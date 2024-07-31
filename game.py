import pygame
import sys
import config
from config import map_config
from config import hero_config
from characters.hero import Hero
from new_map.map_behavior import Map

# Initialize Pygame
pygame.init()

# Use the pre-initialized screen, caption, and clock from config
screen = config.screen
clock = config.clock



hero = Hero(hero_config)

# Create a Map instance
game_map = Map(map_config)

# Main game loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                hero.movement_flags(event)

        

        # Update map offset based on hero's position
        game_map.update_offset(hero.pos_x, hero.pos_y)
      
        game_map.draw()
        
        if game_map.collided_with(hero):
            print("Collision detected")
        else:
            print("No collision detected")

        # Update the hero's position and handle collisions
        hero.master_movement(game_map)

        # Display the hero
        hero.display(screen, game_map.offset_x, game_map.offset_y)
        
        hero.positionInTiles()

        pygame.display.flip()
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

# Entry point
if __name__ == "__main__":
    main()
















