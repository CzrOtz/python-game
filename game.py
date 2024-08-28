#game is not running correctly as of now, do not push

import pygame
import sys
import configurations.config as config
from characters.hero import Hero
from new_map.map_behavior import Map
from characters.ghost_manager import GhostManager
from characters.weapon import Weapon
from configurations.navbar_and_clock import Navbar, GameClock
from configurations.game_difficulty import Difficulty
from characters.collision_manager import CollisionManager
from configurations.power_ups import PowerUpManager
from game_states.game_state import run_game
from game_states.main_menu import main_menu
from game_states.game_over import game_over

state = 1  # Start with the main menu
# Initialize Pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(32)

# Initialize game objects
clock = config.clock
hero = Hero(config.hero_config)
weapon = Weapon(config.hero_weapon_config, hero)
game_map = Map(config.map_config)
navbar = Navbar(config.screen, config.SCREEN_WIDTH, 50, hero, weapon)
ghost_manager = GhostManager(config.ghost_spawn_config, navbar)
collision_manager = CollisionManager(navbar)
power_up_manager = PowerUpManager(config.power_up_manager_config, game_map)
game_clock = navbar.game_clock  # Use the clock from the navbar
difficulty = Difficulty(game_clock, config.ghost_spawn_config, config.ghost_config_template, hero, config.difficulty_config)

# Main game loop
def main():
    global state, hero, weapon, ghost_manager

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = 0  # Set state to 0 to exit the game
                running = False

        print(f'Game in state {state}')
        
        if state == 1:
            state = main_menu(config.screen)
        elif state == 2:
            state = run_game(hero, weapon, game_map, ghost_manager, collision_manager, power_up_manager, difficulty, navbar, clock)
        elif state == 3:
            state = game_over(config.screen)
        
        if state == 0:  # Exit condition
            running = False

        # Reset game objects if returning to main menu
        if state == 1:
            hero.reset()
            weapon = Weapon(config.hero_weapon_config, hero)
            ghost_manager.reset()
            navbar.reset_score()
            game_map.reset()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
























