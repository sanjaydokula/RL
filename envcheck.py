import re
from tkinter.tix import Tree
from SnakeEnv import SnakeEnv


env = SnakeEnv()
episodes = 10


for episode in range(episodes):
    done = False
    # env.done= True
    obs = env.reset()
    print("env.done",env.done)
    while not done:
        random_action = env.action_space.sample()
        print("action", random_action)
        obs,reward,done,info = env.step(random_action)
        print("reward",reward)
        print("done",done)