from SETUPS import *
import random 

class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, position, color="yellow") :
        super().__init__(tetromino.tetris.sprite_group)
        self.color = color
        self.tetromino = tetromino
        self.position = vector(position) + init_position_offset
        self.image = pg.Surface([tile_size, tile_size])
        self.add_border()
        self.alive = True
        self.landed = False
    

    def add_border(self):
        border_size = 2
        pg.draw.rect(self.image, (255,255,255), (1, 1, tile_size - 1, tile_size - 1), border_radius=1)
        pg.draw.rect(self.image, self.color, (border_size, border_size, tile_size - 2*border_size, tile_size - 2*border_size), border_radius=1)
        self.rect = self.image.get_rect()
        
    def remove_border(self):
        pg.draw.rect(self.image, self.color, (1, 1, tile_size - 1, tile_size - 1), border_radius=1)
        self.rect = self.image.get_rect() 

    def is_alive(self):
        if not self.alive:
            self.kill()

    def is_collide(self, pos):
        x, y = int(pos.x), int(pos.y)
        if 0 <= x < field_w and y < field_h and (y < 0 or not self.tetromino.tetris.field_array[y][x]):
            return False
        return True

    def rotate(self, pivot_point):
        shifted = self.position - pivot_point
        rotated = shifted.rotate(90)
        return rotated + pivot_point 

    def update_rect_position(self):
        self.rect.topleft = self.position*tile_size

    def update(self):
        if self.landed : 
            self.remove_border()
        self.is_alive()
        self.update_rect_position()


        

class Tetromino():
    def __init__(self, tetris) :
        self.tetris = tetris
        self.shape  = random.choice(list(tetrominos.keys()))
        self.color = tetromino_colors[self.shape]
        self.blocks = [Block(self, pos, self.color) for pos in tetrominos[self.shape]]
        self.landing = False

    def is_collide(self, block_positions):
        return any(map(Block.is_collide, self.blocks, block_positions))
    
    def rotate(self):
        pivot_block = self.blocks[0].position
        new_block_positions = [block.rotate(pivot_block) for block in self.blocks]
        is_colid = self.is_collide(new_block_positions)
        
        if not is_colid:
            for i, block in enumerate(self.blocks):
                block.position = new_block_positions[i]

    def move(self, action): # input is a string of selection action
        move_direction = move_directions[action]
        new_block_positions = [block.position + move_direction for block in self.blocks]
        is_colid = self.is_collide(new_block_positions)

        if not is_colid:
            for block in self.blocks:
                block.position += move_direction
        elif action=="down": 
            self.landing = True
            return True
        return False
    
    def move_to_bottom(self):
        for _ in range(field_h):
            landed = self.move("down")
            if landed:
                return True
        return None

    def update(self):
        self.move("down")


