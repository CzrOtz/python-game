import pygame
import pytmx

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
scale = 3
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless Runner Prototype")
clock = pygame.time.Clock()


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
    "pos_x": 500,
    "pos_y": 500,
    "speed": 4,
    "scale": scale,
    "sprite_path": "characters/pngBank/tile_0097.png",
    "screen_width": SCREEN_WIDTH,
    "screen_height": SCREEN_HEIGHT,
}

enemy_1_config = {
    "pos_x": 300,
    "pos_y": 300,
    "speed" : 1.5,
    "scale": scale,
    "sprite_path": "characters/pngBank/tile_0108.png"
}

enemy_2_config = {
    "pos_x": 400,
    "pos_y": 350,
    "speed" : 1.25,
    "scale": scale,
    "sprite_path": "characters/pngBank/tile_0108.png"
}





