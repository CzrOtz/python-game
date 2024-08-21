# config.py
import pygame
import random

#1 for laptop 2 for desktop

settup = "2"
# Screen settings

if settup == "1":
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 700
    scale = 3
elif settup == "2":
    SCREEN_WIDTH = 1500
    SCREEN_HEIGHT = 1100
    scale = 3


FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless War")
clock = pygame.time.Clock()


# Initial number of ghosts
initial_ghost_quantity = 1

level_up_sound = "characters/sounds/level_up.wav"

difficulty_config = {
    "time_between_levels": 45,  # Time in seconds for each difficulty increase
    "spawn_rate_decrement": 100,  # Dee ghost speedcrease spawn rate by 500ms each level
    "speed_increment": 0.2,  # Increas by 0.3 each level
    "attack_power_increment": 0.01,  # Increase ghost attack power by 0.5 each level
    "braking_distance_decrement": 1,  # Decrease braking distance by 5 each level
}

maps = {
    "beta": "new_map/new_world.tmx",
    "testing": "new_map/map_for_testing.tmx",
    "beta2": "new_map/debug1.tmx",
    "beta3": "new_map/beta3.tmx",
    
}

power_up_manager_config = {
    "scale": scale,
    "gray_bottle": "characters/pngBank/tile_0113.png",
    "green_bottle": "characters/pngBank/tile_0114.png",
    "red_bottle": "characters/pngBank/tile_0115.png",
    "blue_bottle": "characters/pngBank/tile_0116.png",
    "max_power_ups": 2,  # Maximum number of power-ups on the screen
    "min_spawn_interval": 5000,  # Minimum interval between spawns in milliseconds
    "max_spawn_interval": 15000,  # Maximum interval between spawns in milliseconds

    # Power-up effects
    "gray_bottle_attack_speed_increase": 3,  # Attack speed increase for gray bottle
    "green_bottle_speed_increase": 1,  # Speed increase for green bottle
    "red_bottle_damage_increase": 5,  # Damage increase for red bottle
    "blue_bottle_health_increase": 20,  # Health increase for blue bottle
    "power_up_lifespan": 10000,  # Power-ups stay on screen for 10 seconds (10,000 ms)
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
    "damage": 35,
    "range": 10,
    "speed": 20,
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










