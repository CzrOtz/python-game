# game.py
import pygame
import sys
import config
from characters.hero import Hero
from characters.enemy import Ghost
from new_map.map_behavior import Map

# Initialize Pygame
pygame.init()

clock = config.clock

# Initialize hero
hero = Hero(config.hero_config)

# Initialize map
game_map = Map(config.map_config)

# Initialize ghosts list with initial ghosts
ghosts = [Ghost(cfg) for cfg in config.ghost_config]

# Set up a custom event to add new ghosts
ADD_GHOST_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_GHOST_EVENT, 5000)  # Add a new ghost every 5000 milliseconds (5 seconds)

# Main game loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == ADD_GHOST_EVENT:
                new_ghost_config = config.generate_ghost_config()
                ghosts.append(Ghost(new_ghost_config))
                print(f'Spawned a new ghost at position ({new_ghost_config["pos_x"]}, {new_ghost_config["pos_y"]})')
            else:
                hero.movement_flags(event)

        # Update map offset based on hero's position
        game_map.update_offset(hero.pos_x, hero.pos_y)

        # Clear the screen
        config.screen.fill((0, 0, 0))

        # Draw the map
        game_map.draw()

        # Update and display each ghost
        for ghost in ghosts:
            ghost.master_movement(hero)
            ghost.display(config.screen, game_map)

        # Update the hero's position and handle collisions
        hero.master_movement(game_map)

        # Display the hero
        hero.display(config.screen, game_map.offset_x, game_map.offset_y)

        pygame.display.flip()
        clock.tick(config.FPS)

        # Check for collisions
        for ghost in ghosts:
            if hero.get_rect().colliderect(ghost.get_rect()):
                print(f'Ghost at ({ghost.pos_x}, {ghost.pos_y}) collided with you')
                # pygame.quit()
                # sys.exit()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


















