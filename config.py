# config.py
import pygame

# Screen settings
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 1000
FPS = 60
scale = 2
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless Runner Prototype")
clock = pygame.time.Clock()

# Initial number of ghosts
initial_ghost_quantity = 1

maps = {
    "beta": "new_map/new_world.tmx",
    "testing": "new_map/map_for_testing.tmx",
    "beta2": "new_map/newer_map.tmx",
    "beta3": "new_map/beta3.tmx",
    "beta4": "new_map/beta4.tmx",
    "beta5": "new_map/beta5.tmx",
}

map_config = {
    "tilemap_path": maps["beta3"],
    "pixelalpha": True,
    "scale": scale,
    "screen_width": SCREEN_WIDTH,
    "screen_height": SCREEN_HEIGHT,
    "layer_name": "walls",
    "object_type": "wall",
    "screen": screen,
}

hero_config = {
    "pos_x":200,
    "pos_y": 205,
    "speed": 2,
    "scale": scale,
    "sprite_path": "characters/pngBank/tile_0097.png",
    "screen_width": SCREEN_WIDTH,
    "screen_height": SCREEN_HEIGHT,
    
    
}

hero_weapon_config = {
    "damage": 34,
    "range": 10,
    "speed": 35,
    "scale": scale - 1.2,
    "sprite_path": "characters/pngBank/tile_0131.png",
    "pointer_sp": "characters/pngBank/tile_0101.png",
    "cooldown": 500,
    "position_x": hero_config["pos_x"],
    "position_y": hero_config["pos_y"],
    "sound": "characters/sounds/Arrow2.wav",
}


ghost_spawn_config = {
    "initial_ghost_quantity": 1,
    "spawn_rate": 2500,
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
        "hit_by_weapon": "characters/sounds/hit_marker2.wav",
        "spawn_sound": "characters/sounds/Ghost_gone_4.wav",
        "gone_sound": "characters/sounds/Ghost_spawn2.wav",
    }









