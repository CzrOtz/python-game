import pygame
import sys
import config
from characters.hero import Hero
from characters.enemy import Ghost, Enemy
from new_map.map_behavior import Map

# Initialize Pygame
pygame.init()

# Use the pre-initialized screen, caption, and clock from config
screen = config.screen
clock = config.clock

# Initialize hero
hero = Hero(config.hero_config)

"""ghost_config is the list that holds the dictionary that holds the ghost's attributes"""
"""list comprehension is used to create a list of Ghost objects"""
ghosts = [Ghost(i) for i in config.ghost_config]

game_map = Map(config.map_config)

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
        
        hero.master_movement(game_map)

        # Update and display each ghost
        for i in ghosts:
            i.master_movement(hero)
            i.display(screen, game_map)
        
        

        # Display the hero
        hero.display(screen, game_map.offset_x, game_map.offset_y)

        pygame.display.flip()
        clock.tick(config.FPS)

       
        for i in ghosts:
            if hero.get_rect().colliderect(i.get_rect()):
                print("You died")
                pygame.quit()
                sys.exit()
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

















