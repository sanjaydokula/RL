import cv2
import gym
from gym import spaces
import numpy as np
print("env starting")


colors = {
    'b':(255,0,0),
    'g':(0,255,0),
    'r':(0,0,255)
}

def collision_with_package(fork_position,package_position):
    if abs(fork_position[0] - package_position[0] ) == 10 and (fork_position[1] == package_position[1]) or abs(fork_position[1]+10):
        pass

class WareHouseEnv(gym.Env):
    
    def __inti__(self):
        super(WareHouseEnv,self).__init()

        self.action_space = spaces.Discrete(8)

        self.observation_space = spaces.Box(low=-500,high=500,shape=(4,))

    def step(self,action):
        cv2.imshow("warehouse",self.image)
        self.image = np.zeros((500,500,3),dtype='uint8')

        cv2.rectangle(self.image,(self.fork_position[0],self.fork_position[1]),(self.fork_position[0]+10,self.fork_position[1]+10),(255,0,0),3,cv2.LINE_AA)
        cv2.rectangle(self.image,(self.package[0],self.package[1]),(self.package[0]+10,self.package[1]+10),(0,255,0),3,cv2.LINE_AA)
        cv2.rectangle(self.image,(self.dest_position[0],self.dest_position[1]),(self.dest_position[0]+100,self.dest_position[1]+100),(0,255,0),3,lineType=cv2.LINE_AA)

        if action == 1: #right
            self.fork_position[0]+=10
        elif action == 0: #left
            self.fork_position[0]-=10
        elif action == 2: #down
            self.fork_position[1]+=10
        elif action == 3: #up
            self.fork_position[1]-=10
        elif action == 4: #up-right
            self.fork_position[0]+=10
            self.fork_position[1]-=10
        elif action == 5: #up-left
            self.fork_position[0]-=10
            self.fork_position[1]-=10
        elif action == 6: #down-right
            self.fork_position[0]+=10
            self.fork_position[1]+=10
        elif action == 7: #down-left
            self.fork_position[0]-=10
            self.fork_position[1]+=10

    def reset(self):
        self.image = np.zeros((500,500,3),dtype='uint8')
        self.fork_position = [250,250]
        self.package = [np.random.randint(low=10,high=50)*10,np.random.randint(low=10,high=50)*10]
        self.dest_position = [0,0]
        self.score = 0
        self.reward = 0
        self.button_direction = 1
        self.done = False

        fork_x = self.fork_position[0]
        fork_y = self.fork_position[1]
        package_delta_x = self.package[0] - fork_x
        package_delta_y = self.package[1] - fork_y

        '''

        ++++ delta to the dest from fork or package??
        
        '''



        self.observation = [fork_x,fork_y,package_delta_x,package_delta_y]
        cv2.rectangle(self.image,(self.fork_position[0],self.fork_position[1]),(self.fork_position[0]+10,self.fork_position[1]+10),colors.get('b'),3,lineType=cv2.LINE_AA)
        cv2.rectangle(self.image,(self.package[0],self.package[1]),(self.package[0]+10,self.package[1]+10),colors.get('g'),3,lineType=cv2.LINE_AA)
        
        cv2.rectangle(self.image,(self.dest_position[0],self.dest_position[1]),(self.dest_position[0]+100,self.dest_position[1]+100),colors.get('g'),3,lineType=cv2.LINE_AA)
        cv2.imshow("warehouse",self.image)
        cv2.waitKey(500)

warehouse = WareHouseEnv()
print(colors.get('b'))
warehouse.reset()
cv2.waitKey(10000)