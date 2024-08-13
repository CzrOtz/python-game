import pygame
import sys
import config
from characters.hero import Hero
from characters.hero import deploy_hero
from new_map.map_behavior import Map
from characters.spawner import GhostManager
from characters.spawner import deploy_ghosts
from characters.weapon import Weapon
from additional_inspect import analyze_weapon_movement
from additional_inspect import view_masks




# Initialize Pygame
pygame.init()

clock = config.clock

# Initialize hero
hero = Hero(config.hero_config)

weapon = Weapon(config.hero_weapon_config, hero)

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
                weapon.launch_attack(event, game_map.offset_x, game_map.offset_y)
                
        game_map.update_offset(hero.pos_x, hero.pos_y)
        game_map.draw()
        
        deploy_hero(hero, game_map, config.screen, game_map.offset_x, game_map.offset_y)
        # deploy_ghosts(hero, game_map, weapon, ghost_manager)
        
        weapon.display(config.screen, game_map.offset_x, game_map.offset_y)
        weapon.update_position(hero)
        weapon.fire(hero, game_map.map_width, game_map.map_height, game_map)

        # game_map.draw_mask(config.screen)
        # weapon.draw_mask(config.screen, game_map.offset_x, game_map.offset_y)

        view_masks(game_map, hero, weapon, ghost_manager, config.screen)

        # weapon.inspect()
        

      
        
        pygame.display.flip()
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()



















