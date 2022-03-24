from ast import arg
from cgitb import reset
from re import M
import torch
import gym
from stable_baselines3 import A2C,PPO
import os
from SnakeEnv import SnakeEnv
import cv2
import sys




class Model():

    def __init__(self,*args):

        self.models_dir = "models/PPO-1647365718"
        # self.env = SnakeEnv()
        if len(args)>0 and isinstance(args[0],str):
            print("1 arg and model arg")
            print(f"Selecting {args[0]} model")
            self.model_name = args[0]
        else:
            print("selecting default model")
            self.model_name = "1920000.zip"

        self.model_path = f"{self.models_dir}/{self.model_name}"

        if len(args)>1 and isinstance(args[1],str):
            print("2 arg and env arg")
            if args[1] == "Snake Environment":
                print("selecting snake env")
                self.env = SnakeEnv()
            elif args[1] ==  "MountainCar Environment":
                print("selecting mountain car env")
                self.env = gym.make("MountainCar-v0")
        else:
            print("default env selecting")
            self.env = SnakeEnv()
            self.env.reset()

        self.model = PPO.load(self.model_path, env=self.env)
        self.episodes = 50

        
    def run(self):
        for ep in range(self.episodes):
            obs = self.env.reset()
            done = False
            while not done:
                # env.render()
                action, _ = self.model.predict(obs)
                obs, reward, done, info = self.env.step(action)
                key = cv2.waitKey(50)
                if key == ord('q'):
                    sys.exit()
        self.env.close()