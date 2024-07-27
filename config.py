import pygame
import pytmx

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (75, 48, 50)

# Initialize Pygame components
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless Runner Prototype")
clock = pygame.time.Clock()

# Path to sprite sheet
SPRITESHEET_PATH = 'new_map/tilemap_packed.png'  # Ensure this path is correct

# Path to tile map
TILEMAP_PATH = 'new_map/new_world.tmx'  # Ensure this path is correct







