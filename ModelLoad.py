from cgitb import reset
from re import M
import torch
import gym
from stable_baselines3 import A2C,PPO
import os
from SnakeEnv import SnakeEnv
import cv2



class Model():

    def __init__(self):

        self.models_dir = "models/PPO-1647365718"
        self.model_path = f"{self.models_dir}/1920000.zip"

        self.env = SnakeEnv()
        self.env.reset()

        self.model = PPO.load(self.model_path, env=self.env)
        self.episodes = 50
        # self.load_model()
    # def load_model(self):
    #     return self.model
    def run(self):
        for ep in range(self.episodes):
            obs = self.env.reset()
            done = False
            while not done:
                # env.render()
                action, _ = self.model.predict(obs)
                obs, reward, done, info = self.env.step(action)
                cv2.waitKey(50)
        self.env.close()