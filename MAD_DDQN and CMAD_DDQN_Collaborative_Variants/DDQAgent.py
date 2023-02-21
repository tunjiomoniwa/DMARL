import os
import numpy as np
import torch as T
from torch.utils.tensorboard.writer import SummaryWriter
from DeepQNetwork import DeepQNetwork
from replay_memory import ReplayBuffer

class DoubleDQAgent():
    def __init__(self, lr:float, gamma:float, obs_dims,
                 num_actions:int, mem_size, mini_batchsize,
                 epsilon_dec, env_name, algo_name, epsilon=1.0, replace=1000,
                 epsilon_min=0.1, checkpoint_dir='results\\doubledqn'):

        self.lr = lr
        self.gamma = gamma
        self.obs_dims = obs_dims
        self.num_actions = num_actions
        self.mini_batchsize = mini_batchsize
        self.epsilon_min = epsilon_min
        self.epsilon_dec = epsilon_dec
        self.epsilon = epsilon
        self.replace_target_cnt = replace
        
        self.mem_counter = 0
        self.copy_counter = 0
        self.checkpoint_dir = checkpoint_dir
        self.memories = ReplayBuffer(mem_size=mem_size, 
                                      state_shape=self.obs_dims,
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
        
        self.loss_value = 0
        self.writer = SummaryWriter(os.path.join(self.checkpoint_dir, 'logs'))

    def decrement_epsilon(self):
        if self.epsilon > self.epsilon_min:
            self.epsilon = self.epsilon - self.epsilon_dec
        else:
            self.epsilon = self.epsilon_min
    
    def store_memory(self, obs, action, reward, new_obs, done):
        self.memories.store(obs, action, reward, new_obs, done)
        self.mem_counter += 1

    def sample_memory(self):
        states, actions, rewards, new_states, dones = self.memories.sample(self.mini_batchsize)

        states = T.tensor(states).to(self.target_network.device)
        actions = T.tensor(actions).to(self.target_network.device)
        rewards = T.tensor(rewards).to(self.target_network.device)
        new_states = T.tensor(new_states).to(self.target_network.device)
        dones = T.tensor(dones).to(self.target_network.device)

        # print(f'---States shape: {states.size()}')
        return states, actions, rewards, new_states, dones

    def get_action(self, obs, epsilon):
        if np.random.random() < epsilon:
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
        states, actions, rewards, new_states, dones = self.sample_memory()

        indices = np.arange(self.mini_batchsize)
        q_pred = self.learning_network.forward(states)[indices, actions]
        
        q_next = self.learning_network.forward(new_states)
        actions_selected = T.argmax(q_next, dim=1) # Action selection based on online weights

        q_eval = self.target_network.forward(new_states)  
        q_eval[dones] = 0.0   #Actions' return value are evaluated

        q_target = rewards + self.gamma * q_eval[indices, actions_selected]
        cost = self.learning_network.loss(q_target, q_pred)
        cost.backward()
        self.learning_network.optimizer.step()

        self.decrement_epsilon()

        if self.copy_counter % self.replace_target_cnt == 0:
            self.copy_target_network()
        self.copy_counter += 1
        
        self.loss_value = cost
        
    def log(self, num_episode):
        diff = 0
        for p_learning, p_target in zip(self.learning_network.parameters(), self.target_network.parameters()):
            p_learning = p_learning.data.cpu()
            p_target = p_target.data.cpu()
            diff += T.sum(p_learning - p_target)
            
        self.writer.add_scalar("td_error", self.loss_value, num_episode)
        self.writer.add_scalar("learning_target_diff", diff, num_episode)
        
        return diff
        
    def copy_target_network(self):
        self.target_network.load_state_dict(self.learning_network.state_dict())

    def save_models(self):
        self.learning_network.save()
        self.target_network.save()
    
    def load_models(self):
        self.learning_network.load()
        self.target_network.load()
