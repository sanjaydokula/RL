import gym
import numpy as np
import math as m
from numpy import average
import matplotlib.pyplot as plt
import pickle
# from numpy import block 
from SnakeEnv import SnakeEnv
import time

env = gym.make("MountainCar-v0")
# env = SnakeEnv()
# env = gym.make("CartPole-v1")
# env = gym.make("LunarLander-v2")
alpha = 0.1
discount = .95
episodes = 30000
show_every = 500
epsilon = .6
start_epsilon_decay = 1
end_epsilon_decay = episodes//2
q_table = None

epsilon_decay_value = epsilon/(end_epsilon_decay - start_epsilon_decay)

discrete_obs_size = [10] * len(env.observation_space.low)
print(env.observation_space.high)
print(len(env.observation_space.low))
print(env.action_space.n)
discrete_obs_wind_size = (env.observation_space.high - env.observation_space.low) / discrete_obs_size
# discrete_obs_wind_size = (np.array([m.pow(2,31)]*8) - (np.array([-m.pow(2,31)]*8))) / discrete_obs_size
print(discrete_obs_size)
print(discrete_obs_wind_size)
print(len(discrete_obs_size+[env.action_space.n]))
if q_table is None:
    # initialize the q-table#

    q_table = np.random.uniform(low=-2, high=0, size=(discrete_obs_size + [env.action_space.n]))

else:
    with open(q_table, "rb") as f:
        q_table = pickle.load(f)



def get_discrete_state(state):
    discrete_state = (state-env.observation_space.low) / discrete_obs_wind_size
    return tuple(discrete_state.astype(int))
discrete_state = get_discrete_state(env.reset())

metrics = {'ep':[], 'avg':[], 'min':[], 'max':[]}
ep_rewards = []

for episode in range(episodes):
    episode_reward = 0
    discrete_state = get_discrete_state(env.reset())
    # env.reset()
    done = False
    
    if episode%show_every == 0:
        print(episode)
        render = True
    else:
        render = False
    
    while not done:

        if np.random.random()>epsilon:
            action = np.argmax(q_table[discrete_state])
        else:
            action = np.random.randint(0,env.action_space.n)
        
        new_state, reward, done, info = env.step(action)
        new_discrete_state = get_discrete_state(new_state)
        episode_reward+=reward
        # print(new_state)
        if render:
            env.render()
        if not done:
            max_future_q = np.max(q_table[new_discrete_state])
            current_q = q_table[discrete_state + (action,)]
            new_q = (1-alpha) * current_q + alpha * ( reward + discount * max_future_q)
            q_table[discrete_state + (action,)] = new_q
        # elif new_state[0]>=env.goal_position:
            # print(f"made it on episode {episode}")
            # q_table[discrete_state + (action,)]=0

        discrete_state = new_discrete_state
    ep_rewards.append(episode_reward)
    if end_epsilon_decay >= episode >= start_epsilon_decay:
        epsilon-=epsilon_decay_value
    if not episode%show_every:
        average_reward = sum(ep_rewards[-show_every:])/show_every
        metrics['ep'].append(episode)
        metrics['max'].append(max(ep_rewards[-show_every:]))
        metrics['min'].append(min(ep_rewards[-show_every:]))
        metrics['avg'].append(average_reward)
env.close()


plt.plot(metrics['ep'],metrics['avg'],label="average")
plt.plot(metrics['ep'],metrics['min'],label="min")
plt.plot(metrics['ep'],metrics['max'],label="max")
plt.legend(loc=1)
plt.show()


with open(f"qtable-{int(time.time())}.pickle", "wb") as f:
    pickle.dump(q_table, f)