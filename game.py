import pygame
import sys
import configurations.config as config
from characters.hero import Hero
from characters.hero import deploy_hero
from new_map.map_behavior import Map
from characters.ghost_manager import GhostManager
from characters.weapon import Weapon
from configurations.navbar_and_clock import Navbar, GameClock
from configurations.game_difficulty import Difficulty
from characters.collision_manager import CollisionManager
from configurations.power_ups import PowerUpManager


# Initialize Pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(32)

clock = config.clock

# Initialize hero
hero = Hero(config.hero_config)

# Initialize weapon
weapon = Weapon(config.hero_weapon_config, hero)

# Initialize map
game_map = Map(config.map_config)

# Initialize Navbar and GameClock
navbar = Navbar(config.screen, config.SCREEN_WIDTH, 50, hero, weapon)

# Initialize GhostManager
ghost_manager = GhostManager(config.ghost_spawn_config, navbar)

# Initialize CollisionManager
collision_manager = CollisionManager(navbar)

# Initialize PowerUpManager

#config.power_ups needs to be passed to this right here
power_up_manager = PowerUpManager(config.power_up_manager_config, game_map)

game_clock = navbar.game_clock  # Use the clock from the navbar

# Initialize Difficulty
difficulty = Difficulty(game_clock, config.ghost_spawn_config, config.ghost_config_template, hero, config.difficulty_config)

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
        ghost_manager.update_position(hero, game_map)

        # Handle collisions
        collision_manager.check_hero_ghost_collisions(hero, ghost_manager.ghosts)
        collision_manager.check_weapon_ghost_collisions(weapon, ghost_manager.ghosts)

        weapon.display(config.screen, game_map.offset_x, game_map.offset_y)
        weapon.update_position(hero)
        weapon.fire(game_map.map_width, game_map.map_height, game_map)

        # Power-up management
        power_up_manager.update()
        power_up_manager.check_collisions(hero, weapon)
        power_up_manager.display(config.screen, game_map.offset_x, game_map.offset_y)

        # Check and update the difficulty based on time
        difficulty.check_and_update_difficulty()
        difficulty.render_level_display(config.screen)

        # Hero and weapon are passed because their attributes (like speed and damage) are dynamic.
        # Since no modifications are made to hero or weapon within the Navbar class itself,
        # the render method always requires the current state of hero and weapon to be passed in.
        # The values stored in the Navbar instance are the initial values and won't update automatically.
        navbar.render(hero, weapon)

        pygame.display.flip()
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()






















