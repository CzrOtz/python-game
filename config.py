# config.py
import pygame

# Screen settings
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 900
FPS = 60
scale = 3
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless Runner Prototype")
clock = pygame.time.Clock()

# Initial number of ghosts
initial_ghost_quantity = 1

maps = {
    "beta": "new_map/new_world.tmx",
    "testing": "new_map/map_for_testing.tmx",
}

map_config = {
    "tilemap_path": maps["beta"],
    "pixelalpha": True,
    "scale": scale,
    "screen_width": SCREEN_WIDTH,
    "screen_height": SCREEN_HEIGHT,
    "layer_name": "walls",
    "object_type": "wall",
    "screen": screen,
}

hero_config = {
    "pos_x":160,
    "pos_y": 205,
    "speed": 2,
    "scale": scale,
    "sprite_path": "characters/pngBank/tile_0097.png",
    "screen_width": SCREEN_WIDTH,
    "screen_height": SCREEN_HEIGHT,
    
    
}

hero_weapon_config = {
    "damage": 10,
    "range": 10,
    "speed": 20,
    "scale": scale - 1.2,
    "sprite_path": "characters/pngBank/tile_0131.png",
    "pointer_sp": "characters/pngBank/tile_0101.png",
    "cooldown": 500,
    "position_x": hero_config["pos_x"],
    "position_y": hero_config["pos_y"]
}




ghost_spawn_config = {
    "initial_ghost_quantity": 1,
    "spawn_rate": 5000,
    "screen": screen,
    "scale": scale, 
}

# def generate_ghost_config():
#     return {
#         "pos_x": 500,
#         "pos_y": 1500,
#         "speed": 1.5,
#         "scale": scale,
#         "sprite_path": "characters/pngBank/tile_0109.png",
#         "braking_distance": 150,
#         "r_number_min": 0,
#         "r_number_max": 6,
#         "health": 100
#     }




ghost_spawn_config = {
    "initial_ghost_quantity": 1,
    "spawn_rate": 5000,
    "screen": screen,
    "scale": scale, 
}

def generate_ghost_config():
    return {
        "pos_x": 500,
        "pos_y": 1500,
        "speed": 1.5,
        "scale": scale,
        "sprite_path": "characters/pngBank/tile_0108.png",
        "braking_distance": 150,
        "r_number_min": 0,
        "r_number_max": 6,
        "health": 100,
        "hit_by_weapon": "characters/sounds/hit_marker.wav"
    }









