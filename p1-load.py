from cgitb import reset
from re import M
import torch
import gym
from stable_baselines3 import A2C,PPO
import os
from SnakeEnv import SnakeEnv
import cv2


models_dir = "models/PPO-1646917910"
model_path = f"{models_dir}/970000.zip"
env = SnakeEnv()
env.reset()

model = PPO.load(model_path, env=env)

episodes = 50

for ep in range(episodes):
    obs = env.reset()
    done = False

    while not done:
        # env.render()
        action, _ = model.predict(obs)
        obs, reward, done, info = env.step(action)
        cv2.waitKey(50)
env.close()