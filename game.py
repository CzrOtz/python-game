import pygame
import sys
import config
from characters.hero import Hero
from characters.hero import deploy_hero
from new_map.map_behavior import Map
from characters.spawner import GhostManager
from characters.spawner import deploy_ghosts
from characters.weapon import Weapon

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
                weapon.launch_attack(event)
                
                
                

        game_map.update_offset(hero.pos_x, hero.pos_y)
        game_map.draw()
        
        

        deploy_hero(hero, game_map, config.screen, game_map.offset_x, game_map.offset_y)


        weapon.display(config.screen, game_map.offset_x, game_map.offset_y)
        weapon.update_position(hero)
        weapon.fire(hero)

        weapon.inspect()
        


        deploy_ghosts(hero, game_map, weapon, ghost_manager)

        
        pygame.display.flip()
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()



















