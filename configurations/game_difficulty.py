import pygame
from configurations.navbar_and_clock import GameClock  # Assuming your GameClock class is in this module

class Difficulty:
    def __init__(self, game_clock: GameClock):
        self.game_clock = game_clock
        self.difficulty_level = 1  # Initial difficulty level
        self.last_level_up_time = 0  # Last time the difficulty was increased

    def check_and_update_difficulty(self):
        """Update difficulty based on the elapsed time."""
        hours, minutes, seconds = self.game_clock.get_elapsed_time()
        total_minutes = hours * 60 + minutes

        # Increase difficulty every 5 minutes, for example
        if total_minutes > self.last_level_up_time + 5:
            self.difficulty_level += 1
            self.last_level_up_time = total_minutes
            self.apply_difficulty_changes()

    def apply_difficulty_changes(self):
        """Apply changes to the game based on the current difficulty level."""
        print(f"Difficulty level increased to {self.difficulty_level}!")
        # Increase the enemy spawn rate
        self.enemy_config["spawn_rate"] = max(1000, self.enemy_config["spawn_rate"] - 200)

        

    def get_difficulty_level(self):
        """Return the current difficulty level."""
        return self.difficulty_level
