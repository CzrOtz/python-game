import pygame
import random
from enemy import Ghost
from config import generate_ghost_config
from config import ghost_spawn_config

class GhostManager:
    def __init__(self, config):
        self.ghosts = []
        self.screen = config["screen"]
        self.scale = config["scale"]
        self.spawn_rate = config["spawn_rate"]
        self.add_ghost_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.add_ghost_event, self.spawn_rate)  # Add a new ghost every `spawn_rate` milliseconds
        self.initial_ghost_quantity = config["initial_ghost_quantity"]
        self.generate_initial_ghosts()

    def generate_initial_ghosts(self):
        for _ in range(self.initial_ghost_quantity):
            self.ghosts.append(Ghost(generate_ghost_config(self.scale)))

    def update(self, hero, game_map):
        for ghost in self.ghosts:
            ghost.master_movement(hero)
            ghost.display(self.screen, game_map)

    def add_new_ghost(self):
        new_ghost_config = generate_ghost_config(self.scale)
        self.ghosts.append(Ghost(new_ghost_config))
        print(f'Spawned a new ghost at position ({new_ghost_config["pos_x"]}, {new_ghost_config["pos_y"]})')

    def check_collisions(self, hero):
        for ghost in self.ghosts:
            if hero.get_rect().colliderect(ghost.get_rect()):
                print(f'Ghost at ({ghost.rect.x}, {ghost.rect.y}) collided with you')
                # Handle collision (e.g., increase score, end game, etc.)