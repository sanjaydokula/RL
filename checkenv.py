from stable_baselines3.common.env_checker import check_env
from SnakeEnv import SnakeEnv


env = SnakeEnv()
# It will check your custom environment and output additional warnings if needed
check_env(env)