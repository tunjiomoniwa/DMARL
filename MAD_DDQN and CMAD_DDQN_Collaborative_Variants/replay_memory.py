import numpy as np

class ReplayBuffer():
    def __init__(self, mem_size, state_shape, num_actions):
        self.mem_size = mem_size
        self.memory_count = 0
        #self.state_shape = state_shape

        self.state_memory = np.zeros((self.mem_size, state_shape),
                                      dtype=np.float32)
        #self.state_memory = np.zeros(state_shape, dtype=np.float32)
        self.action_memory = np.zeros(self.mem_size, dtype=np.int64)
        self.reward_memory = np.zeros(self.mem_size, dtype=np.float32)
        self.new_state_memory = np.zeros((self.mem_size, state_shape), dtype=np.float32)
        #self.new_state_memory = np.zeros(state_shape, dtype=np.float32)
        self.done_memory = np.zeros(self.mem_size, dtype=np.bool)

    def store(self, state, action, reward, new_state, done):
        id = self.memory_count % self.mem_size
        self.state_memory[id] = state
        self.action_memory[id] = action
        self.reward_memory[id] = reward
        self.new_state_memory[id] = new_state
        self.done_memory[id] = done
        self.memory_count += 1
        
        #if not done:
            #self.state_memory.append(state)
        #self.action_memory.append(action)
        #self.reward_memory.append(reward)
        #self.new_state_memory.append(new_state)
        #self.done_memory.append(done)
    
    def sample(self, mini_batchsize):
        current_size = min(self.memory_count, self.mem_size)
        idx = np.random.choice(current_size, mini_batchsize, replace=False)
        
        states = self.state_memory[idx]
        actions = self.action_memory[idx]
        rewards = self.reward_memory[idx]
        new_states = self.new_state_memory[idx]
        dones = self.done_memory[idx]

        # print(f'---Actions: {actions}')
        return states, actions, rewards, new_states, dones
