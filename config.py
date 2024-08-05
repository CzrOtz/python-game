# Existing configuration settings
import pygame
import random

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
scale = 3
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless Runner Prototype")
clock = pygame.time.Clock()
speed_increment = 0.0001
speed_limit = 2
ghost_quantity = 5

map_config = {
    "tilemap_path": "new_map/new_world.tmx",
    "pixelalpha": True,
    "scale": scale,
    "screen_width": SCREEN_WIDTH,
    "screen_height": SCREEN_HEIGHT,
    "layer_name": "walls",
    "object_type": "wall",
    "screen" : screen,
}

hero_config = {
    "pos_x": 700,
    "pos_y": 500,
    "speed": 4,
    "scale": scale,
    "sprite_path": "characters/pngBank/tile_0097.png",
    "screen_width": SCREEN_WIDTH,
    "screen_height": SCREEN_HEIGHT,
    "weapon": "characters/pngBank/tile_0103.png",
    "weapon_speed": 10
}

"""this piece of code 
    appends the dictionary into a list a certain ammount of times before the main game loop starts
"""
def generate_ghost_configs(num_ghosts):
    storage = []
    for i in range(num_ghosts):
        config = {
            "pos_x": random.randint(0, SCREEN_WIDTH),
            "pos_y": random.randint(0, SCREEN_HEIGHT),
            "speed": 1.5,
            "scale": scale,
            "sprite_path": "characters/pngBank/tile_0108.png",
            "increment": speed_increment,
            "speed_limit": speed_limit,
            "braking_distance": 100,
            "r_number_min": 0,
            "r_number_max": 6,
        }
        storage.append(config)
    return storage


ghost_config = generate_ghost_configs(ghost_quantity)






