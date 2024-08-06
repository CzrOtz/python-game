import pygame
import sys
import config
from characters.hero import Hero
from new_map.map_behavior import Map
from characters.spawner import GhostManager

# Initialize Pygame
pygame.init()

clock = config.clock

# Initialize hero
hero = Hero(config.hero_config)

# Initialize map
game_map = Map(config.map_config)

# Initialize GhostManager

ghost_manager = GhostManager(config.ghost_spawn_config)

# Main game loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == ghost_manager.add_ghost_event:
                ghost_manager.add_new_ghost()
            else:
                hero.movement_flags(event)

        game_map.update_offset(hero.pos_x, hero.pos_y)
        game_map.draw()
        
        hero.master_movement(game_map)
        hero.display(config.screen, game_map.offset_x, game_map.offset_y)
        ghost_manager.update_position(hero, game_map)
        ghost_manager.check_collisions(hero)

        # config.screen.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()



















