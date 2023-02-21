import numpy as np
import gym
from gym.spaces import Box
from gym.wrappers import TimeLimit
import cv2
import collections

'''
Objectives:
1. Go from 3 channels to 1 (grayscale)
2. Resize img to 84x84
3. Take max of previous 2 frames
4. Repeat action 4 times
5. Swap channels to first axis
6. Stack 4 most recent frames
7. Scale inputs /255

class RepeatActionAndMaxFrame
Handles action repeat and take max of 2 frames

class PreprocessFrame
Handles grayscale, reshaping and data scaling

class StackFrames
Handles frame stacking

'''

class RepeatActionAndMaxFrame(gym.Wrapper):
    def __init__(self, env, clip_reward, no_ops, fire_first, num_repeat=4):
        super().__init__(env)
        self.num_repeat = num_repeat
        self.obs_space = env.observation_space.shape
        self.frame_buffer = [np.empty(self.obs_space, dtype=np.uint8),
                             np.empty(self.obs_space, dtype=np.uint8)]
        self.clip_reward = clip_reward
        self.no_ops = no_ops
        self.fire_first = fire_first

    def step(self, action):
        total_reward = 0
        done = False
        for i in range(self.num_repeat):
            new_obs, reward, done, info = self.env.step(action) 
            if self.clip_reward:
                reward = np.clip(np.array([reward]), -1, 1)[0]
            total_reward += reward
            
            idx = i % 2
            self.frame_buffer[idx] = new_obs
            if done:
                break
        max_frame = np.maximum(self.frame_buffer[0], self.frame_buffer[1])
        return max_frame, total_reward, done, info
        
    def reset(self):
        obs = self.env.reset()
        if self.no_ops != 0:
            no_ops = np.random.randomint(self.no_ops) + 1
        if self.fire_first:
            assert self.env.unwrapped.get_action_meanings()[1] == 'FIRE'
            obs, _, _, _ = self.env.step(1)
        
        self.frame_buffer = [np.empty(self.obs_space, dtype=np.uint8),
                             np.empty(self.obs_space, dtype=np.uint8)]
        self.frame_buffer[0] = obs

        return obs

class PreprocessFrame(gym.ObservationWrapper):
    def __init__(self, env, shape):
        super().__init__(env)
        self.shape = (shape[2], shape[0], shape[1])
        self.observation_space = gym.spaces.Box(low=0.0, high=1.0,
                                                shape=self.shape, dtype=np.float32)
        # gym.spaces.Box describes an env dealing with real valued quantities
        # arguments are the lower-bounds and higher-bounds

    def observation(self, obs):
        obs_gray = cv2.cvtColor(obs, cv2.COLOR_BGR2GRAY)
        resized_screen = cv2.resize(obs_gray, self.shape[1:],
                                    interpolation=cv2.INTER_AREA)
        obs_reshaped = np.array(resized_screen, dtype=np.uint8).reshape(self.shape)
        obs_rescaled = obs_reshaped / 255.0

        return obs_reshaped

class StackFrames(gym.ObservationWrapper):
    def __init__(self, env, num_repeat=4):
        super().__init__(env)
        self.observation_space = gym.spaces.Box(low=env.observation_space.low.repeat(num_repeat, axis=0),
                                                high=env.observation_space.high.repeat(num_repeat, axis=0),
                                                dtype=np.float32)
        self.queue = collections.deque(maxlen=num_repeat)
        self.num_repeat = num_repeat
    
    def reset(self):
        self.queue.clear()
        observation = self.env.reset()
        for _ in range(self.num_repeat):
            self.queue.append(observation)
            
        return np.array(self.queue).reshape(self.observation_space.low.shape)

    def observation(self, observation):
        self.queue.append(observation)
        return np.array(self.queue).reshape(self.observation_space.low.shape)
    

def make_env(env_name, shape=(84, 84, 1), num_repeat=4, clip_reward=False, no_ops=0, fire_first=False):
    env = gym.make(env_name)
    env = RepeatActionAndMaxFrame(env, clip_reward, no_ops, fire_first, num_repeat=num_repeat)
    env = PreprocessFrame(env, shape=shape)
    env = StackFrames(env, num_repeat=num_repeat)

    return env

