import pygame

"""
Navbar observes Hero parameters -> no Navbar calls in Hero class
Navabr observes Weapon parameters -> no Navbar calls in Weapon class

GhosManager class modifies Navbar -> 3 calls from GhostManager to Navbar
enemies_on_screen +/-= 1
kill_count += 1

"""

# Navbar Class
class Navbar:
    def __init__(self, screen, width, height, hero, weapon,font_size=24, bg_color=(0, 0, 0), font_color=(255, 255, 255)):
        self.screen = screen
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.font_color = font_color
        self.font = pygame.font.Font(None, font_size)

        # Initialize variables
        self.kill_count = 0  # Enemy kill count
        self.hero_speed = hero.speed  # Hero speed (placeholder)
        # self.weapon_range = "n/a"  # Weapon range (placeholder)
        self.weapon_damage = weapon.damage  # Weapon damage (placeholder)
        self.hero_health = hero.health  # Hero health (placeholder)
        self.enemies_on_screen = 1  # Enemies on screen (placeholder)

        # Initialize the GameClock
        self.game_clock = GameClock(screen, font_size, font_color)

    def update_stats(self, kill_count=None, hero_speed=None, weapon_range=None, weapon_damage=None, hero_health=None, enemies_on_screen=None):
        """Update the statistics displayed in the navbar."""
        if kill_count is not None:
            self.kill_count = kill_count
        if hero_speed is not None:
            self.hero_speed = hero_speed
        # if weapon_range is not None:
        #     self.weapon_range = weapon_range
        if weapon_damage is not None:
            self.weapon_damage = weapon_damage
        if hero_health is not None:
            self.hero_health = hero_health
        if enemies_on_screen is not None:
            self.enemies_on_screen = enemies_on_screen

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

        # # Render the weapon range next to the hero speed
        # weapon_range_string = f"Weapon Range: {self.weapon_range}"
        # weapon_range_surface = self.font.render(weapon_range_string, True, self.font_color)
        # start_x += hero_speed_surface.get_width() + 20  # Move x position for the next stat
        # self.screen.blit(weapon_range_surface, (start_x, y_position))

        # Render the weapon damage next to the weapon range
        weapon_damage_string = f"Weapon Damage: {self.weapon_damage}"
        weapon_damage_surface = self.font.render(weapon_damage_string, True, self.font_color)
        start_x += hero_speed_surface.get_width() + 20  # Move x position for the next stat
        self.screen.blit(weapon_damage_surface, (start_x, y_position))

        # Render the hero health next to the weapon damage
        hero_health_string = f"Hero Health: {self.hero_health}"
        hero_health_surface = self.font.render(hero_health_string, True, self.font_color)
        start_x += weapon_damage_surface.get_width() + 20  # Move x position for the next stat
        self.screen.blit(hero_health_surface, (start_x, y_position))

        # Render the enemies on screen next to the hero health
        enemies_on_screen_string = f"Enemies on Screen: {self.enemies_on_screen}"
        enemies_on_screen_surface = self.font.render(enemies_on_screen_string, True, self.font_color)
        start_x += hero_health_surface.get_width() + 20  # Move x position for the next stat
        self.screen.blit(enemies_on_screen_surface, (start_x, y_position))

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