import numpy as np

class ReplayBufferTeacher():
    def __init__(self, mem_size, state_shape, aug_size, num_actions):
        self.mem_size = mem_size
        self.aug_size = aug_size
        self.memory_count = 0

        self.state_memory = np.zeros((self.mem_size, *state_shape),
                                      dtype=np.float32)
        self.aug_states_memory = np.zeros((self.mem_size, aug_size, *state_shape),
                                      dtype=np.float32)
        self.action_memory = np.zeros((self.mem_size), dtype=np.int64)
        self.reward_memory = np.zeros(self.mem_size, dtype=np.float32)
        self.new_state_memory = np.zeros((self.mem_size, *state_shape), dtype=np.float32)
        self.done_memory = np.zeros(self.mem_size, dtype=np.bool)

    def store(self, state, aug_states, action, reward, new_state, done):
        id = self.memory_count % self.mem_size
        # for i in range(self.aug_size):
        #     aug_states = np.concatenate((aug_states, state), axis=0)

        self.state_memory[id] = state
        self.aug_states_memory[id] = aug_states #aug_states is a list of augmented states along with same number of original
        self.action_memory[id] = action
        self.reward_memory[id] = reward
        self.new_state_memory[id] = new_state
        self.done_memory[id] = done

        self.memory_count += 1
    
    def sample(self, mini_batchsize):
        current_size = min(self.memory_count, self.mem_size)
        idx = np.random.choice(current_size, mini_batchsize, replace=False)
        
        states = self.state_memory[idx]
        aug_states = self.aug_states_memory[idx]
        # aug_states_flattened = aug_states.reshape()
        actions = self.action_memory[idx]
        rewards = self.reward_memory[idx]
        new_states = self.new_state_memory[idx]
        dones = self.done_memory[idx]

        # print(f'---Actions: {actions}')
        return states, aug_states, actions, rewards, new_states, dones