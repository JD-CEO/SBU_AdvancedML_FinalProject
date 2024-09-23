from SETUPS import *
from tetris import Tetris
import sys


class Application():
    def __init__(self, mode="training"):
        pg.init()
        pg.display.set_caption("Tetris")
        self.screen = pg.display.set_mode(field_res)
        self.tetris = Tetris(self)
        self.tick = None 
        self.is_over = False

    '''
        Down below three components of the game is defined that are : 
            1- actions handling 
            2- updating game components 
            3- rendering the result 
    '''
    def check_event(self, action):
        act_reward = 0 
        act_reward += self.tetris.control(action)
        return act_reward


    def update(self):
        rewards = self.tetris.update()
        return rewards

    def draw(self):
        self.screen.fill(color=field_color)
        self.tetris.draw()
        pg.display.flip()

    def step(self, action):
        act_reward = self.check_event(action)
        rewards = self.update()
        self.draw() #This can be optional
        return [act_reward , rewards]

