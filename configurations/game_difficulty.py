import pygame
from configurations.navbar_and_clock import GameClock
import configurations.config as config  # Import the ghost config template

class Difficulty:
    def __init__(self, game_clock: GameClock, enemy_config, ghost_config_template, hero, difficulty_config):
        self.game_clock = game_clock
        self.enemy_config = enemy_config  # Config for spawn rate adjustment
        self.ghost_config_template = ghost_config_template  # Config for individual ghost attributes
        self.hero = hero  # Pass the hero object to access its speed
        self.difficulty_level = 1  # Initial difficulty level
        self.last_level_up_time = 0  # Last time the difficulty was increased
        self.difficulty_config = difficulty_config  # Configuration for difficulty adjustments

        # Load the level-up sound effect
        self.level_up_sound = pygame.mixer.Sound(config.level_up_sound)

        # Font and position for the level display
        self.font = pygame.font.Font(None, 36)
        self.level_display_duration = 2000  # Duration in milliseconds to show the level text
        self.level_display_start_time = None  # When the level display started

    def check_and_update_difficulty(self):
        """Update difficulty based on the elapsed time."""
        hours, minutes, seconds = self.game_clock.get_elapsed_time()
        total_seconds = hours * 3600 + minutes * 60 + seconds

        # Increase difficulty based on the configured time interval
        if total_seconds > self.last_level_up_time + self.difficulty_config["time_between_levels"]:
            self.difficulty_level += 1
            self.last_level_up_time = total_seconds
            self._apply_difficulty_changes()

    def _apply_difficulty_changes(self):
        """Apply changes to the game based on the current difficulty level."""
        # Play the level-up sound
        self.level_up_sound.play()
        

        # Decrease the enemy spawn rate
        self._decrease_spawn_rate()

        # Increase speed
        self._increase_speed()

        # Increase attack power
        self._increase_attack_power()

        # Decrease braking distance
        self._decrease_braking_distance()

        # Start displaying the level-up text
        self.level_display_start_time = pygame.time.get_ticks()

    def render_level_display(self, screen):
        """Render the level-up text if within the display duration."""
        if self.level_display_start_time:
            elapsed_time = pygame.time.get_ticks() - self.level_display_start_time
            if elapsed_time < self.level_display_duration:
                level_text = f"Level: {self.difficulty_level}"
                text_surface = self.font.render(level_text, True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
                screen.blit(text_surface, text_rect)
            else:
                self.level_display_start_time = None  # Stop displaying after the duration

    def _decrease_spawn_rate(self):
        """Decrease the spawn rate by the configured decrement."""
        decrement = self.difficulty_config["spawn_rate_decrement"]
        new_spawn_rate = max(1000, self.enemy_config["spawn_rate"] - decrement)
        self.enemy_config["spawn_rate"] = new_spawn_rate
        pygame.time.set_timer(pygame.USEREVENT + 1, new_spawn_rate)

    def _increase_speed(self):
        """Increase the speed of ghosts, but not exceed the hero's speed."""
        increment = self.difficulty_config["speed_increment"]
        new_speed = self.ghost_config_template["speed"] + increment

        # Ensure ghost speed does not exceed hero speed
        if new_speed > self.hero.speed:
            new_speed = self.hero.speed

        self.ghost_config_template["speed"] = new_speed

    def _increase_attack_power(self):
        """Increase the attack power of ghosts."""
        increment = self.difficulty_config["attack_power_increment"]
        self.ghost_config_template["attack_power"] = self.ghost_config_template.get("attack_power", 0) + increment

    def _decrease_braking_distance(self):
        """Decrease the braking distance of ghosts."""
        decrement = self.difficulty_config["braking_distance_decrement"]
        self.ghost_config_template["braking_distance"] = max(10, self.ghost_config_template["braking_distance"] - decrement)

    def inspect(self):
        """Inspect the current state of the difficulty settings."""
        inspection_details = {
            "difficulty_level": self.difficulty_level,
            "enemy_spawn_rate": self.enemy_config["spawn_rate"],
            "ghost_speed": self.ghost_config_template["speed"],
            "ghost_attack_power": self.ghost_config_template.get("attack_power", 0),
            "ghost_braking_distance": self.ghost_config_template["braking_distance"],
            "time_since_last_level_up": pygame.time.get_ticks() - self.last_level_up_time
        }
        return inspection_details

    def get_difficulty_level(self):
        """Return the current difficulty level."""
        return self.difficulty_level










