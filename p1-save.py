from cgitb import reset
from re import M
import torch
import gym
from stable_baselines3 import A2C,PPO
import os
import time

from SnakeEnv import SnakeEnv


env = SnakeEnv()
model_name = "PPO"
models_dir = f"models/{model_name}-{int(time.time())}"
logidr = f"logs/{model_name}-{int(time.time())}"

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(models_dir):
    os.makedirs(models_dir)


# env = gym.make("LunarLander-v2")

env.reset()

TIMESTEPS = 10000

model = PPO("MlpPolicy", env, verbose=1, tensorboard_log=logidr)

for i in range(1,100):
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=model_name)
    model.save(f"{models_dir}/{TIMESTEPS*i}")



env.close()