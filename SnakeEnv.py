from pickletools import uint8
import gym
from gym import spaces
import cv2
import numpy as np
import random
import time
from collections import deque

SNAKE_LEN_GOAL = 50

def collision_with_apple(apple_position, score):
	apple_position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
	score += 1
	return apple_position, score

def collision_with_boundaries(snake_head):
    if snake_head[0]>=500 or snake_head[0]<0 or snake_head[1]>=500 or snake_head[1]<0:
        # print("collided")
        return 1
    else:
        return 0

def collision_with_self(snake_position):
    snake_head = snake_position[0]
    if snake_head in snake_position[1:]:
        # print('collided with body')
        return 1
    else:
        return 0


N_DISCRETE_ACTIONS = 4
N_CHANNELS = None
HEIGHT = None
WIDTH = None

class SnakeEnv(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(SnakeEnv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
        # Example for using image as input (channel-first; channel-last also works):
        self.observation_space = spaces.Box(low=-500, high=500,
                                            shape=(5+SNAKE_LEN_GOAL,), dtype=np.float32)

    def step(self, action):
        self.prev_actions.append(action)
        # cv2.imshow("Snake",self.image)
        # cv2.waitKey(50)
        # self.image = np.zeros((500,500,3),dtype='uint8')

        # # test the tuple(self.apple_position) in rectangle
        # cv2.rectangle(self.image,(self.apple_position[0],self.apple_position[1]),(self.apple_position[0]+10,self.apple_position[1]+10),(0,0,255),3)

        # for pos in self.snake_position:
            # print("snek")
            # cv2.rectangle(self.image,(pos[0],pos[1]),(pos[0]+10,pos[1]+10),(0,255,0),3)
        #     # print(self.snake_position)
        #     # cv2.waitKey(1000)

        self.render()
        time_to_take_step = time.time() + 0.05
        k= -1
        while time.time() > time_to_take_step:
            if k == -1:
                k = cv2.waitKey(1)
            else:
                continue
        # try changing +=10 to +=5 if somthing is not working properly
        if action == 1:
            self.snake_head[0]+=10
        elif action == 0:
            self.snake_head[0]-=10
        elif action == 2:
            self.snake_head[1]+=10
        elif action == 3:
            self.snake_head[1]-=10


        # if action == 1 and self.previous_button_direction !=0:
        #     self.snake_head[0]+=10
        # elif action == 0 and self.previous_button_direction !=1:
        #     self.snake_head[0]-=10
        # elif action == 2 and self.previous_button_direction !=3:
        #     self.snake_head[1]+=10
        # elif action == 3 and self.previous_button_direction !=2:
        #     self.snake_head[1]-=10
        
        # print("snake head ",self.snake_head)
        apple_reward = 0
        if self.snake_head == self.apple_position:
            # print("at ap",self.snake_position,self.snake_head)
            self.apple_position, self.score = collision_with_apple(self.apple_position,self.score)
            self.snake_position.insert(0,list(self.snake_head))
            apple_reward=10000
            # print("at apple",self.snake_position)
        else:
            # print("at norm",self.snake_position,self.snake_head)
            self.snake_position.insert(0,list(self.snake_head))
            self.snake_position.pop()
            # print("normal",self.snake_position)
        
        if collision_with_boundaries(self.snake_head) == 1 or collision_with_self(self.snake_position) == 1:
            # print("dead")
            font = cv2.FONT_HERSHEY_SIMPLEX
            self.image = np.zeros((500,500,3),dtype='uint8')
            cv2.putText(self.image,'Your Score is {}'.format(self.score),(140,250), font, 1,(255,255,255),2,cv2.LINE_AA)
            cv2.imshow('Snake',self.image)
            # cv2.waitKey(100)
            self.done = True

            # self.total_reward = len(self.snake_position) - 3
            # self.reward = self.total_reward - self.prev_reward
            # self.prev_reward = self.total_reward

        euclidean_dist_apple = np.linalg.norm(np.array(self.snake_head) - np.array(self.apple_position))
        self.total_reward = ((250 - euclidean_dist_apple) + apple_reward)/100

            # self.reward = self.total_reward - self.prev_reward
            # self.prev_reward = self.total_reward
        if self.done:
            self.total_reward = -10
        info = {}


        head_x = self.snake_head[0]
        head_y = self.snake_head[1]

        snake_length = len(self.snake_position)
        apple_delta_x = self.apple_position[0] - head_x
        apple_delta_y = self.apple_position[1] - head_y

        # create observation:

        self.observation = [head_x, head_y, apple_delta_x, apple_delta_y, snake_length] + list(self.prev_actions)
        self.observation = np.array(self.observation)


        return self.observation, self.total_reward, self.done, info


    def reset(self):
        self.image = np.zeros((500,500,3),dtype='uint8')
        self.snake_position = [[250,250],[240,250],[230,250]]
        self.apple_position = [np.random.randint(low=1,high=50)*10,np.random.randint(low=1,high=50)*10]    
        self.score = 0
        self.reward = 0
        self.previous_button_direction = 1
        self.button_direction = 1
        self.snake_head = [250,250]

        self.prev_reward = 0
        self.done = False
        head_x = self.snake_head[0]
        head_y = self.snake_head[1]
        
        snake_length = len(self.snake_position)

        apple_delta_x = self.apple_position[0] - head_x
        apple_delta_y = self.apple_position[1] - head_y

        self.prev_actions = deque(maxlen=SNAKE_LEN_GOAL)
        for i in range(SNAKE_LEN_GOAL):
            self.prev_actions.append(-1)
        
        self.observation = [head_x, head_y, apple_delta_x, apple_delta_y, snake_length] + list(self.prev_actions)
        self.observation = np.array(self.observation)
        return self.observation  # reward, done, info can't be included

    def render(self):
        cv2.imshow("Snake",self.image)
        cv2.waitKey(50)
        self.image = np.zeros((500,500,3),dtype='uint8')
        cv2.rectangle(self.image,(self.apple_position[0],self.apple_position[1]),(self.apple_position[0]+10,self.apple_position[1]+10),(0,0,255),3)
        for pos in self.snake_position:
            # print("snek")
            cv2.rectangle(self.image,(pos[0],pos[1]),(pos[0]+10,pos[1]+10),(0,255,0),3)
