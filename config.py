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
    "pos_x": 100,
    "pos_y": 100,
    "speed": 4,
    "scale": scale,
    "sprite_path": "characters/pngBank/tile_0097.png",
}




