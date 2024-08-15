import pygame
import sys
import config
from characters.hero import Hero
from characters.hero import deploy_hero
from new_map.map_behavior import Map
from characters.spawner import GhostManager
from characters.spawner import deploy_ghosts
from characters.weapon import Weapon
from additional_inspect import view_masks

# Navbar Class
class Navbar:
    def __init__(self, screen, width, height, font_size=24, bg_color=(0, 0, 0), font_color=(255, 255, 255)):
        self.screen = screen
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.font_color = font_color
        self.font = pygame.font.Font(None, font_size)

        # Initialize variables
        self.kill_count = 0  # Enemy kill count
        self.hero_speed = 0  # Hero speed (placeholder)
        self.weapon_range = 0  # Weapon range (placeholder)
        self.weapon_damage = 0  # Weapon damage (placeholder)
        
        # Initialize the GameClock
        self.game_clock = GameClock(screen, font_size, font_color)

    def update_stats(self, kill_count=None, hero_speed=None, weapon_range=None, weapon_damage=None):
        """Update the statistics displayed in the navbar."""
        if kill_count is not None:
            self.kill_count = kill_count
        if hero_speed is not None:
            self.hero_speed = hero_speed
        if weapon_range is not None:
            self.weapon_range = weapon_range
        if weapon_damage is not None:
            self.weapon_damage = weapon_damage

    def render(self):
        """Render the navbar with all stats."""
        # Draw the navbar background
        pygame.draw.rect(self.screen, self.bg_color, pygame.Rect(0, 0, self.width, self.height))

        # Starting position for rendering the stats
        start_x = 10
        y_position = self.height // 2 - 10  # Align text vertically at the center of the navbar

        # Render the clock
        hours, minutes, seconds = self.game_clock.get_elapsed_time()
        time_string = f"{hours:02}:{minutes:02}:{seconds:02}"
        time_surface = self.font.render(time_string, True, self.font_color)
        self.screen.blit(time_surface, (start_x, y_position))

        # Render the kill count next to the clock
        kill_count_string = f"Kills: {self.kill_count}"
        kill_count_surface = self.font.render(kill_count_string, True, self.font_color)
        start_x += time_surface.get_width() + 20  # Move x position for the next stat
        self.screen.blit(kill_count_surface, (start_x, y_position))

        # Render the hero speed next to the kill count
        hero_speed_string = f"Hero Speed: {self.hero_speed}"
        hero_speed_surface = self.font.render(hero_speed_string, True, self.font_color)
        start_x += kill_count_surface.get_width() + 20  # Move x position for the next stat
        self.screen.blit(hero_speed_surface, (start_x, y_position))

        # Render the weapon range next to the hero speed
        weapon_range_string = f"Weapon Range: {self.weapon_range}"
        weapon_range_surface = self.font.render(weapon_range_string, True, self.font_color)
        start_x += hero_speed_surface.get_width() + 20  # Move x position for the next stat
        self.screen.blit(weapon_range_surface, (start_x, y_position))

        # Render the weapon damage next to the weapon range
        weapon_damage_string = f"Weapon Damage: {self.weapon_damage}"
        weapon_damage_surface = self.font.render(weapon_damage_string, True, self.font_color)
        start_x += weapon_range_surface.get_width() + 20  # Move x position for the next stat
        self.screen.blit(weapon_damage_surface, (start_x, y_position))

# GameClock Class
class GameClock:
    def __init__(self, screen, font_size=24, color=(255, 255, 255)):
        self.start_time = pygame.time.get_ticks()  # Record the start time
        self.screen = screen
        self.font = pygame.font.Font(None, font_size)  # Use default font
        self.color = color

    def get_elapsed_time(self):
        """Calculate the elapsed time since the start of the game."""
        elapsed_time_ms = pygame.time.get_ticks() - self.start_time
        seconds = (elapsed_time_ms // 1000) % 60
        minutes = (elapsed_time_ms // (1000 * 60)) % 60
        hours = elapsed_time_ms // (1000 * 60 * 60)
        return hours, minutes, seconds

    def render(self):
        """Render the elapsed time on the screen."""
        hours, minutes, seconds = self.get_elapsed_time()
        time_string = f"{hours:02}:{minutes:02}:{seconds:02}"
        time_surface = self.font.render(time_string, True, self.color)
        self.screen.blit(time_surface, (10, 10))  # Draw in the top-left corner


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

# Initialize Navbar
navbar = Navbar(config.screen, config.SCREEN_WIDTH, 50)  # Height of 50 pixels for the navbar

# Main game loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == ghost_manager.add_ghost_event:
                ghost_manager.add_new_ghost()
                pass
            else:
                hero.movement_flags(event)
                weapon.launch_attack(event, game_map.offset_x, game_map.offset_y)

        game_map.update_offset(hero.pos_x, hero.pos_y)
        game_map.draw()

        deploy_hero(hero, game_map, config.screen, game_map.offset_x, game_map.offset_y)
        deploy_ghosts(hero, game_map, weapon, ghost_manager)

        weapon.display(config.screen, game_map.offset_x, game_map.offset_y)
        weapon.update_position(hero)
        weapon.fire(hero, game_map.map_width, game_map.map_height, game_map)

        # Render the navbar
        navbar.render()

        pygame.display.flip()
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()




















