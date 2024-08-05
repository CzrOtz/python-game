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



hero = Hero(config.hero_config)
ghost1 = Ghost(config.ghost_1_config)
ghost2 = Ghost(config.ghost_2_config)


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
        ghost1.master_movement(hero)
        ghost2.master_movement(hero)


        # Display the hero
        hero.display(screen, game_map.offset_x, game_map.offset_y)
        ghost1.display(screen, game_map)
        ghost2.display(screen, game_map)

        #screen, game_map, config.ghost_1_config, hero
        
        # hero.positionInTiles()

        # enemy.inspect(hero, game_map)

        pygame.display.flip()
        clock.tick(config.FPS)

        if hero.get_rect().colliderect(ghost1.get_rect()):
            print("You died")
            pygame.quit()
            sys.exit()
        
       

    pygame.quit()
    sys.exit()




# Entry point
if __name__ == "__main__":
    main()
















