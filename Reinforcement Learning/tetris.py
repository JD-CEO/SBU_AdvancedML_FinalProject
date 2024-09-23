from SETUPS import *
from tet_block import Tetromino
import math
import numpy as np

class Tetris():
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group() # This contains all the blocks of each tetromino class 
        self.field_array = self.get_field_array()
        self.tetromino = Tetromino(self)
        self.num_full_lines = 0
        self.num_steps = 0
        self.acu_lin = 0

    '''
        This function creates first initialized filed array
    '''
    def get_field_array(self):
        return [[0 for _ in range(field_w)] for _ in range(field_h)]
    
    
    '''
        This function puts current tetromino block inside the field array 
    '''
    def put_tetromino_in_field(self):
        for block in self.tetromino.blocks:
            block.landed = True
            column, row = int(block.position.x), int(block.position.y)
            self.field_array[row][column] = block


    '''
        If the game is over then try to restart the game 
    ''' 
    def is_game_over(self):
        for item in self.field_array[0]:
            if item != 0:
                return True
        return False

    '''     
        This function checks whether a line is created in any part of the field or not and if it did so it will be removed 
    '''
    def check_full_lines(self):
        pivot_row = field_h - 1
        for row in range(field_h - 1, -1, -1):
            for col in range(field_w - 1, -1, -1):
                self.field_array[pivot_row][col] = self.field_array[row][col]

                if self.field_array[row][col]:
                    self.field_array[pivot_row][col].position = vector(col, row)
            
            if sum(map(bool, self.field_array[row])) < field_w : 
                pivot_row -= 1
            else : 
                for j in range(field_w):
                    self.field_array[pivot_row][j].alive = False
                    self.field_array[pivot_row][j] = 0
                self.num_full_lines += 1
                self.num_full_lines += 1


    def get_num_full_lines(self):
        score = self.num_full_lines
        self.num_full_lines = 0
        return score

    '''
        This function checks whether a tetromino block is landed or not 
            landed :
                - It will put this tetromino block inside the field array 
                - Checks whether the game is over or not :
                    - Yes : Reinitialize the Tetris class 
                    - No : Create a new tetromino block and replace it with previous one 
            not landed :
    '''
    def check_tetromino_landing(self):
        landing_reward = 0
        game_over_reward = 0
        if self.tetromino.landing :
            self.put_tetromino_in_field()
            landing_reward += self.check_num_attached_blocks()
            if self.is_game_over():
                game_over_reward += reward_sys["lose"]
                self.__init__(self.app)
            else: 
                self.tetromino = Tetromino(self)
        return [landing_reward, game_over_reward]

    '''
        This function will return the reward associated to each kind of joints that has been made in the game board 
        By Joint_[number] I mean how many pairs of blocks are next to each other if its joins_2 it means 2 pairs of blocks are next to each other 
        in other words it means 3 blocks were landed next to each other 

    '''
    def check_num_attached_blocks(self):
        reward = 0
        pivot_row = 0 
        for block in self.tetromino.blocks:
            col_b = block.position.x
            row = int(block.position.y)
            reward += (1/row)*reward_sys["hight"] if row > 0 else 0# This penalty is for minimization of the hight of the tetrominos after landing 
            
            if row != pivot_row:
                pivot_row = row
            else:
                continue
            
            joints_2 = 0
            joints_3 = 0
            joints_4 = 0
            joints_5 = 0
            joints_6 = 0
            joints_7 = 0
            joints_8 = 0
            for col in range(field_w - 3, -1, -1):
                if sum(map(bool, self.field_array[row][col: col+3])) == 2 and (col <= col_b <= col+2):
                    joints_2 += 1
            for col in range(field_w - 4, -1, -1):
                if sum(map(bool, self.field_array[row][col: col+4])) == 3 and (col <= col_b <= col+3):
                    joints_3 += 1
            for col in range(field_w - 5, -1, -1):
                if sum(map(bool, self.field_array[row][col: col+5])) == 4 and (col <= col_b <= col+4):
                    joints_4 += 1
            for col in range(field_w - 6, -1, -1):
                if sum(map(bool, self.field_array[row][col: col+6])) == 5 and (col <= col_b <= col+5):
                    joints_5 += 1
            for col in range(field_w - 7, -1, -1):
                if sum(map(bool, self.field_array[row][col: col+7])) == 6 and (col <= col_b <= col+6):
                    joints_6 += 1
            for col in range(field_w - 8, -1, -1):
                if sum(map(bool, self.field_array[row][col: col+8])) == 7 and (col <= col_b <= col+7):
                    joints_7 += 1
            for col in range(field_w - 9, -1, -1):
                if sum(map(bool, self.field_array[row][col: col+9])) == 8 and (col <= col_b <= col+8):
                    joints_8 += 1
            if reward_sys["joints 8"]**joints_8 > 1 : 
                reward += (1/(field_h - row))*reward_sys["joints 8"]**joints_8 
            elif reward_sys["joints 7"]**joints_7 > 1 : 
                reward += (1/(field_h - row))*reward_sys["joints 7"]**joints_7
            elif reward_sys["joints 6"]**joints_6 > 1 : 
                reward += (1/(1.2*(field_h - row)))*reward_sys["joints 6"]**joints_6
            elif reward_sys["joints 5"]**joints_5 > 1 :
                reward += (1/(2*(field_h - row)))*reward_sys["joints 5"]**joints_5
            elif reward_sys["joints 4"]**joints_4 > 1 :
                reward += (1/(2*(field_h - row)))*reward_sys["joints 4"]**joints_4
            elif reward_sys["joints 3"]**joints_3 > 1 :
                reward += (1/(2*(field_h - row)))*reward_sys["joints 3"]**joints_3
            elif reward_sys["joints 2"]**joints_2 > 1 : 
                reward += (1/(2*(field_h - row)))*reward_sys["joints 2"]**joints_2
            else :
                reward += reward_sys["landing"]
        return reward
            
    '''
        This function calculates the number of empty blocks that are in between landed tetrominos 
    '''
    def Calculate_empy_space(self):
        max_idx = 0
        for row in range(field_h):
            if sum(map(bool, self.field_array[row])) > 0:
                max_idx += 1
        num_empty_blocks = field_w*max_idx - sum(map(bool, np.array(self.field_array[field_h - max_idx:][:]).flatten().tolist()))
        return num_empty_blocks

    '''
        This function controls each action and does each action after those action being selected (negative reward for each action)
    '''
    def control(self, action):
        if action == 'left':
            self.tetromino.move('left')
            return reward_sys["left"]
        elif action == 'right':
            self.tetromino.move('right')
            return reward_sys["right"]
        elif action == 'up':
            self.tetromino.rotate()
            return reward_sys["up"]
        elif action == 'down':
            self.tetromino.move_to_bottom()
            return reward_sys["down"]
        elif action == "do nothing":
            return reward_sys["do nothing"]
        return 0


    '''
        This function updates the whole game in each iteration 
            - Defines with what speed should blocks go 
            - If any of those trigers were True then :
                - Checks if there is any full line (return full line reward)
                - Then updates the tetromino blocks which is moving it one block down 
                - Checks whether a tetromino has landed or not and also if the game is over (return game over negative reward and landing negative reward)
    '''
    def update(self): # we can return a dictionary  of full_line_reward, landing_reward, game_over_reward
        self.num_steps += 1
        rewards = {
            "game over" : 0,
            "landing" : 0,
            "score" : 0,
            "num_steps": 0,
            "joints" : 0 ,
            "empty_space" : 0
        }
        # rewards["num_steps"] = -1*(reward_sys["num_steps"]**self.num_steps)
        num_empty_blocks = self.Calculate_empy_space()
        rewards["empty_space"] = -1*(abs(reward_sys["empty_blocks"]**num_empty_blocks)) if num_empty_blocks > 0 else 0
        self.check_full_lines()
        self.tetromino.update()
        rewards["joints"], rewards["game over"] = self.check_tetromino_landing() #rewards["landing"]
        self.get_num_full_lines()
        rewards["score"] = reward_sys["fill_line"]*self.acu_lin # In this part we'll get number of full lines in each step
        self.sprite_group.update()
        return rewards

    '''
        This function draws initial grid of the whole game 
    '''
    def draw_grid(self):
        for i in range(field_w):
            for j in range(field_h):
                pg.draw.rect(self.app.screen, "black", (i*tile_size, j*tile_size, tile_size, tile_size), 1)

    '''
        This function renders state of the board in each step 
    '''
    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)

  