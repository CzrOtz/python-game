import pygame
from characters.enemy import Ghost
from configurations.config import generate_ghost_config

class GhostManager:
    def __init__(self, config, navbar):
        self.config = config
        self.navbar = navbar
        self.reset()

    def reset(self):
        self.ghosts = []
        self.screen = self.config["screen"]
        self.scale = self.config["scale"]
        self.spawn_rate = self.config["spawn_rate"]
        self.add_ghost_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.add_ghost_event, self.spawn_rate)
        self.initial_ghost_quantity = self.config["initial_ghost_quantity"]
        self._generate_initial_ghosts()
        self.navbar.enemies_on_screen = 0

    def _generate_initial_ghosts(self):
        """Generates the initial ghosts based on the configuration."""
        for _ in range(self.initial_ghost_quantity):
            self.ghosts.append(Ghost(generate_ghost_config()))

    def update_position(self, hero, game_map):
        """Updates the position of each ghost."""
        for ghost in self.ghosts:
            ghost.master_movement(hero)
            ghost.display(self.screen, game_map)
            ghost.draw_hit_marker(self.screen, game_map)

    def add_new_ghost(self):
        """Adds a new ghost to the list."""
        new_ghost_config = generate_ghost_config()
        new_ghost = Ghost(new_ghost_config)
        self.ghosts.append(new_ghost)
        new_ghost.spawn_sound.play()  # Play the spawn sound
        self.navbar.enemies_on_screen += 1

    def inspect(self):
        """Prints out detailed information about each ghost in the list."""
        print("----- Ghost List Detailed Inspection -----")
        for idx, ghost in enumerate(self.ghosts):
            print(f"Ghost {idx + 1}:")
            print(f"  - Position: ({ghost.pos_x}, {ghost.pos_y})")
            print(f"  - Health: {ghost.health}")
            print(f"  - Speed: {ghost.speed}")
            print(f"  - Scale: {ghost.scale}")
            print(f"  - Sprite Dimensions: (Width: {ghost.width * ghost.scale}, Height: {ghost.height * ghost.scale})")
            print(f"  - Braking Distance: {ghost.braking_distance}")
            print(f"  - Random Number Range: ({ghost.r_number_min}, {ghost.r_number_max})")
            print(f"  - Speed Modified: {ghost.speed_modified}")
            print(f"  - Original Speed: {ghost.original_speed}")
            print("----------------------")
        print("----- END OF INSPECTION -----\n")
    
    def draw_all_masks(self, game_map):
        """Draws the collision mask of each ghost as a semi-transparent red overlay for debugging."""
        for ghost in self.ghosts:
            ghost.draw_mask(self.screen, game_map)

