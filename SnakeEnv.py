from pickletools import uint8
from this import d
import gym
from gym import spaces
import cv2
import numpy as np
import random
import time
from collection import deque

SNAKE_LEN_GOAL = 50

def collisionWithApple(apple_position):
    pass

N_DISCRETE_ACTIONS = 4
N_CHANNELS = None
HEIGHT = None
WIDTH = None

class CustomEnv(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(CustomEnv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
        # Example for using image as input (channel-first; channel-last also works):
        self.observation_space = spaces.Box(low=0, high=255,
                                            shape=(N_CHANNELS, HEIGHT, WIDTH), dtype=np.uint8)

    def step(self, action):
        self.prev_actions.append(action)
        cv2.imshow("a",self.image)
        return observation, reward, done, info
    def reset(self):
        self.image = np.zeros((500,500,3),dtype=uint8)
        self.snake_position = [[250,250],[240,250],[230,250]]
        self.apple_position = [np.random.randint(low=1,high=100)*5,np.random.randint(low=1,high=100)*5]    
        self.score = 0
        self.previous_button_direction = 1
        self.button_direction = 1
        self.snake_head = self.snake_position[0]

        self.prev_reward = 0
        self.done = False
        head_x = self.snake_head[0]
        head_y = self.snake_head[1]
        snake_length = len(self.snake_position)

        apple_delta_x = self.apple_position[0] - head_x
        apple_delta_y = self.apple_position[1] - head_y
        return observation  # reward, done, info can't be included
    def render(self, mode='human'):
        ...
    def close (self):
        ...