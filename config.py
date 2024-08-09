# config.py
import pygame

# Screen settings
SCREEN_WIDTH = 950
SCREEN_HEIGHT = 950
FPS = 60
scale = 3
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless Runner Prototype")
clock = pygame.time.Clock()

# Initial number of ghosts
initial_ghost_quantity = 1

map_config = {
    "tilemap_path": "new_map/new_world.tmx",
    "pixelalpha": True,
    "scale": scale,
    "screen_width": SCREEN_WIDTH,
    "screen_height": SCREEN_HEIGHT,
    "layer_name": "walls",
    "object_type": "wall",
    "screen": screen,
}

hero_config = {
    "pos_x": 700,
    "pos_y": 850,
    "speed": 4,
    "scale": scale,
    "sprite_path": "characters/pngBank/tile_0097.png",
    "screen_width": SCREEN_WIDTH,
    "screen_height": SCREEN_HEIGHT,
    "weapon": "characters/pngBank/tile_0103.png",
    "weapon_speed": 10
}

hero_weapon_config = {
    "damage": 1,
    "range": 10,
    "speed": 10,
    "scale": scale - 1.2,
    "sprite_path": "characters/pngBank/tile_0131.png",
    "pointer_sp": "characters/pngBank/tile_0101.png",
    "cooldown": 500,
}




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
    }









