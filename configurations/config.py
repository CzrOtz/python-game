# config.py
import pygame
import random

# Screen settings
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 1000
FPS = 60
scale = 4
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless War")
clock = pygame.time.Clock()


# Initial number of ghosts
initial_ghost_quantity = 1

level_up_sound = "characters/sounds/level_up.wav"

difficulty_config = {
    "time_between_levels": 5,  # Time in seconds for each difficulty increase
    "spawn_rate_decrement": 500,  # Dee ghost speedcrease spawn rate by 500ms each level
    "speed_increment": 0.3,  # Increas by 0.3 each level
    "attack_power_increment": 0.3,  # Increase ghost attack power by 0.5 each level
    "braking_distance_decrement": 3,  # Decrease braking distance by 5 each level
}

maps = {
    "beta": "new_map/new_world.tmx",
    "testing": "new_map/map_for_testing.tmx",
    "beta2": "new_map/debug1.tmx",
    "beta3": "new_map/beta3.tmx",
    
}

map_config = {
    "tilemap_path": maps["beta2"],
    "pixelalpha": True,
    "scale": scale,
    "screen_width": SCREEN_WIDTH,
    "screen_height": SCREEN_HEIGHT,
    "layer_name": "walls",
    "object_type": "wall",
    "screen": screen,
}

hero_config = {
    "pos_x":190,
    "pos_y": 250,
    "speed": 2,
    "scale": scale,
    "sprite_path": "characters/pngBank/tile_0097.png",
    "screen_width": SCREEN_WIDTH,
    "screen_height": SCREEN_HEIGHT,
    "health": 100,
    
    
}

hero_weapon_config = {
    "damage": 100,
    "range": 10,
    "speed": 75,
    "scale": scale - 1.2,
    "sprite_path": "characters/pngBank/tile_0131.png",
    "pointer_sp": "characters/pngBank/tile_0101.png",
    "cooldown": 500,
    "position_x": hero_config["pos_x"],
    "position_y": hero_config["pos_y"],
    "sound": "characters/sounds/Arrow2.wav",
    "collision_sound": "characters/sounds/weapon_hit.wav",
}


ghost_spawn_config = {
    "initial_ghost_quantity": 1,
    "spawn_rate": 2500,
    "screen": screen,
    "scale": scale, 
}

ghost_config_template = {
    "pos_x": 0,
    "pos_y": 0,
    "speed": 0.5,
    "scale": scale,
    "sprite_path": "characters/pngBank/tile_0108.png",
    "braking_distance": 200,
    "r_number_min": 1,
    "r_number_max": 6,
    "health": 100,
    "attack_power": 0.5,
    "hit_by_weapon": "characters/sounds/hit_marker2.wav",
    "spawn_sound": "characters/sounds/Ghost_gone_4.wav",
    "gone_sound": "characters/sounds/Ghost_spawn2.wav"
}

def generate_ghost_config():
    map_width = map_config["screen_width"]
    map_height = map_config["screen_height"]

    ghost_config_template["pos_x"] = random.randint(0, map_width - 1)
    ghost_config_template["pos_y"] = random.randint(0, map_height - 1)
    ghost_config_template["scale"] = scale  # Set the actual scale value

    return ghost_config_template










