from main import Application
from SETUPS import *
import numpy as np
from gymnasium import Env , spaces

class Tetris_environment(Env):
    def __init__(self):
        super().__init__()
        # Set the game dynamics 
        self.application = Application()
        
        # Set the initial state 
        self.state_space = spaces.Box(low=0, high=255, shape=(field_res[1], field_res[0], 3), dtype=np.uint8)

        # define action space in this part 
        self.action_space = spaces.Discrete(5)

        # define reward space for better result (its because target domain which effects the network should be bounded)

        # Set thge total colected reward 
        self.total_reward = 0

        self.rewards = {
            "game over" : 0,
            "landing" : 0,
            "score" : 0,
            "num_steps": 0,
            "joints" : 0 
        }
        self.num_steps = 0

    def add_rewards(self, rewards):
        self.num_steps +=1
        self.rewards["game over"] = self.rewards["game over"] + (1/self.num_steps)*(rewards["game over"] - self.rewards["game over"]) 
        self.rewards["landing"] = self.rewards["landing"] + (1/self.num_steps)*(rewards["landing"] - self.rewards["landing"]) 
        self.rewards["score"] = self.rewards["score"] + (1/self.num_steps)*(rewards["score"] - self.rewards["score"]) 
        self.rewards["num_steps"] = self.rewards["num_steps"] + (1/self.num_steps)*(rewards["num_steps"] - self.rewards["num_steps"]) 
        self.rewards["joints"] = self.rewards["joints"] + (1/self.num_steps)*(rewards["joints"] - self.rewards["joints"]) 


    def step(self, action):
        done = False
        reward = 0
        info = {}
        act_reward , rewards = self.application.step(action)
        state = pg.surfarray.array3d(self.application.screen)

        reward += rewards["score"] + rewards["game over"] + rewards["joints"] + rewards["empty_space"]
        # act_reward + sum(rewards.values())

        # self.add_rewards(rewards)
        if rewards["game over"] < 0:
            done = True
        else : 
            # because the block is still alive Ill give it a +1 reward for that 
            reward += reward_sys["being alive"]
        
        return state, reward, done, False, info

    def reset(self):
        pg.quit()
        self.application = Application()
        self.application.step("do nothing")
        state = pg.surfarray.array3d(self.application.screen)
        return state
    
    def close(self):
        pg.display.quit()
        pg.quit()
