import pygame
from configurations import config
from characters.hero import deploy_hero

def run_game(hero, weapon, game_map, ghost_manager, collision_manager, power_up_manager, difficulty, navbar, clock):
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
        navbar.render(hero, weapon)

        # Check for game over condition
        if hero.health <= 0:
            print("Hero health is 0 or less. Transitioning to Game Over.")
            return 3  # Return the game over state
        
        pygame.display.flip()
        clock.tick(config.FPS)