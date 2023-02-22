import os
import numpy as np
import torch as T
from torch.utils.tensorboard.writer import SummaryWriter
from DeepQNetwork import DeepQNetwork
from replay_memory_teacher import ReplayBufferTeacher
from skimage.util import random_noise

class MeanTeacherAgent(): # Double DQN with Mean Teacher semi-supervised learning strategy
    def __init__(self, lr:float, gamma:float, obs_dims, 
                 num_actions:int, mem_size, mini_batchsize,
                 epsilon_dec, env_name, algo_name, epsilon=1.0, replace=1000,
                 epsilon_min=0.1, aug_size=4, random_noise_std=0.1, checkpoint_dir='results\\MeanTeacherDDQN'):

        self.lr = lr
        self.gamma = gamma
        self.obs_dims = obs_dims
        self.aug_size = aug_size
        self.num_actions = num_actions
        self.mini_batchsize = mini_batchsize
        self.epsilon_min = epsilon_min
        self.epsilon_dec = epsilon_dec
        self.epsilon = epsilon
        self.replace_target_cnt = replace
        
        self.mem_counter = 0
        self.copy_counter = 0
        self.checkpoint_dir = checkpoint_dir
        self.memories = ReplayBufferTeacher(mem_size=mem_size, 
                                     state_shape=self.obs_dims,
                                     aug_size=aug_size,
                                     num_actions=self.num_actions)
        self.action_space = [i for i in range(self.num_actions)]

        self.learning_network = DeepQNetwork(lr=self.lr, 
                              num_actions=self.num_actions,
                              input_dims=self.obs_dims, 
                              name=algo_name+'_'+env_name+'_'+'learning', 
                              checkpoint_dir=self.checkpoint_dir)

        self.target_network = DeepQNetwork(lr=self.lr, 
                              num_actions=self.num_actions,
                              input_dims=self.obs_dims, 
                              name=env_name+'_'+algo_name+'_target', 
                              checkpoint_dir=self.checkpoint_dir)

        self.teacher_network = DeepQNetwork(lr=self.lr, 
                              num_actions=self.num_actions,
                              input_dims=self.obs_dims, 
                              name=algo_name+'_'+env_name+'_'+'teacher', 
                              checkpoint_dir=self.checkpoint_dir)

        self.random_noise_std = random_noise_std
        self.online_cost = 0
        self.teacher_cost = 0
        self.writer = SummaryWriter(os.path.join(self.checkpoint_dir, 'logs'))

    def decrement_epsilon(self):
        if self.epsilon > self.epsilon_min:
            self.epsilon = self.epsilon - self.epsilon_dec
        else:
            self.epsilon = self.epsilon_min
    
    def augment_state(self, obs):
        aug_states = []
        for i in range(self.aug_size):
            aug_states.append(random_noise(obs, var=self.random_noise_std**2))
        return aug_states
    
    def store_memory(self, obs, action, reward, new_obs, done):
        aug_states = self.augment_state(obs)
        self.memories.store(obs, aug_states, action, reward, new_obs, done)
        self.mem_counter += 1

    def sample_memory(self):
        _states, _aug_states, _actions, _rewards, _new_states, _dones = self.memories.sample(self.mini_batchsize)

        _states = T.tensor(_states)
        _aug_states = T.tensor(_aug_states)
        _actions = T.tensor(_actions)
        _rewards = T.tensor(_rewards)
        _new_states = T.tensor(_new_states)
        _dones = T.tensor(_dones)

        states = T.tensor(_states).to(self.target_network.device)
        actions = T.tensor(_actions).to(self.target_network.device)
        rewards = T.tensor(_rewards).to(self.target_network.device)
        new_states = T.tensor(_new_states).to(self.target_network.device)
        dones = T.tensor(_dones).to(self.target_network.device)

        # Flattens augmented states into batchsize of minibatch_size * aug_size, the others are repeated
        _aug_states = _aug_states.reshape((_aug_states.shape[0]*_aug_states.shape[1], *self.obs_dims))
        teacher_states = _aug_states.to(self.target_network.device)
        teacher_actions = T.tensor(T.repeat_interleave(_actions.clone(), repeats=self.aug_size, dim=0)).to(self.target_network.device)
        teacher_rewards = T.tensor(T.repeat_interleave(_rewards.clone(), repeats=self.aug_size, dim=0)).to(self.target_network.device)
        teacher_new_states = T.tensor(T.repeat_interleave(_new_states.clone(), repeats=self.aug_size, dim=0)).to(self.target_network.device)
        teacher_dones = T.tensor(T.repeat_interleave(_dones.clone(), repeats=self.aug_size, dim=0)).to(self.target_network.device)
        
        # print(f'---Teacher States shape: {teacher_states.size()}')
        return states,actions,rewards,new_states,dones,teacher_states,teacher_actions,teacher_rewards,teacher_new_states,teacher_dones

    def get_action(self, obs):
        if np.random.random() < self.epsilon:
            action = np.random.choice(len(self.action_space), 1)[0]
        else:
            state = T.tensor([obs], dtype=T.float).to(self.learning_network.device)

            returns_for_actions = self.target_network.forward(state)
            action = T.argmax(returns_for_actions).cpu().detach().numpy()
        return action
    
    def learn(self):
        if self.mem_counter < self.mini_batchsize:
            return
        
        self.learning_network.optimizer.zero_grad()
        self.teacher_network.optimizer.zero_grad()
        states,actions,rewards,new_states,dones,teacher_states,teacher_actions,teacher_rewards,teacher_new_states,teacher_dones = self.sample_memory()

        # === Learning for online net === #
        indices = np.arange(self.mini_batchsize)
        q_pred = self.learning_network.forward(states)[indices, actions]
        
        q_next = self.learning_network.forward(new_states)
        actions_selected = T.argmax(q_next, dim=1) # Action selection based on online weights

        q_eval = self.target_network.forward(new_states)  
        q_eval[dones] = 0.0   #Actions' return value are evaluated

        q_target = rewards + self.gamma * q_eval[indices, actions_selected]
        online_cost = self.learning_network.loss(q_target, q_pred)
        online_cost.backward()
        self.learning_network.optimizer.step()

        # ==== Learning for teacher net ==== #
        indices = np.arange(self.mini_batchsize * self.aug_size)
        q_pred = self.teacher_network.forward(teacher_states)[indices, teacher_actions]
        
        q_next = self.teacher_network.forward(teacher_new_states)
        actions_selected = T.argmax(q_next, dim=1) # Action selection based on online weights

        q_eval = self.target_network.forward(teacher_new_states)  
        q_eval[teacher_dones] = 0.0   #Actions' return value are evaluated

        q_target = teacher_rewards + self.gamma * q_eval[indices, actions_selected]
        teacher_cost = self.teacher_network.loss(q_target, q_pred)
        teacher_cost.backward()
        self.teacher_network.optimizer.step()

        self.decrement_epsilon()
        if self.copy_counter % self.replace_target_cnt == 0:
            self.copy_target_network()
        self.copy_counter += 1

        self.online_cost = online_cost
        self.teacher_cost = teacher_cost
        
        
    def log(self, num_episode):
        diff = 0
        for p_online, p_teacher in zip(self.learning_network.parameters(), self.teacher_network.parameters()):
            p_online = p_online.data.cpu()
            p_teacher = p_teacher.data.cpu()
            diff += T.sum(p_online - p_teacher)
            
        self.writer.add_scalar("Online td_error", self.online_cost, num_episode)
        self.writer.add_scalar("Teacher td_error", self.teacher_cost, num_episode)
        self.writer.add_scalar("online_teacher_diff", diff, num_episode)
        
        return diff
        
    def copy_target_network(self):
        self.target_network.load_state_dict(self.learning_network.state_dict())

    def save_models(self):
        self.learning_network.save()
        self.target_network.save()
    
    def load_models(self):
        self.learning_network.load()
        self.target_network.load()