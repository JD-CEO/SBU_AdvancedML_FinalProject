import pygame as pg 


vector = pg.math.Vector2


field_color =  (48, 39, 32)
tile_size = 15 
field_size = field_w, field_h = 10, 20
field_res = field_w *tile_size ,field_h*tile_size
init_position_offset = vector(field_w// 2 - 1, 1) 

tetromino_colors = {
    'T': (235,164,0),
    'O': (212,49,13),
    'J': (152,255,0),
    'L': (0, 255, 64),
    'I': (0,212,255),
    'S': (21,0,255),
    'Z': (230,0,255)
}

tetrominos = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}


move_directions = {'left': vector(-1, 0), 'right': vector(1, 0), 'down': vector(0, 1)} # action space 


reward_sys = {
    "joints 2":1.01,
    "joints 3":1.04,
    "joints 4":1.08,
    "joints 5":1.1,
    "joints 6":1.4,
    "joints 7":1.5,
    "joints 8":1.7,
    "landing" : -1.5,
    "hight" : -50, # -40
    "lose" : -30, # -30
    "fill_line" : 100, #100
    "being alive":1,
    "empty_blocks":-1.025,
    "up" : -0.5,
    "down" : -0.5,
    "left" : -0.5,
    "right" : -0.5,
    "do nothing": -4,
    "landing_on_top":-1.07,
    "num_steps":-1.07,
}

