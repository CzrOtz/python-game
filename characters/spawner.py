import pygame
import random
from characters.enemy import Ghost
from config import generate_ghost_config


"""this class depends on the Ghost class and the generate_ghost_config function from config.py"""

"""ghosts is every instance of the ghost class that is within the []"""

"""ghost_config """

class GhostManager:
    def __init__(self, config):
        self.ghosts = []
        self.screen = config["screen"]
        self.scale = config["scale"]
        self.spawn_rate = config["spawn_rate"]
        self.add_ghost_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.add_ghost_event, self.spawn_rate)  # Add a new ghost every `spawn_rate` milliseconds
        self.initial_ghost_quantity = config["initial_ghost_quantity"]
        self._generate_initial_ghosts()

    """this method generatges the initial ghosts"""
    """this is a private method only used once in the constructor"""    
    def _generate_initial_ghosts(self):
        for _ in range(self.initial_ghost_quantity):
            self.ghosts.append(Ghost(generate_ghost_config()))

    """this method applies the master movement method to each ghost in the list"""
    #the character that the player is controlling OR you want the ghost to follow
    #and the map the ghost is in
    def update_position(self, hero, game_map):
        for ghost in self.ghosts:
            ghost.master_movement(hero)
            ghost.display(self.screen, game_map)
    
    """this method adds a new ghost to the list"""
    #this method is in the game loop in the event loop
    def add_new_ghost(self):
        new_ghost_config = generate_ghost_config()

        #this is where the dictionary is being paired with the ghost
        self.ghosts.append(Ghost(new_ghost_config))

        # print(f'Spawned a new ghost at position ({new_ghost_config["pos_x"]}, {new_ghost_config["pos_y"]})')

    """this method applies the collision check to each ghost in the list"""
    def check_collisions(self, hero, weapon):
        for ghost in self.ghosts:
            if hero.get_rect().colliderect(ghost.get_rect()):
                # print(f'Ghost at ({ghost.pos_x}, {ghost.pos_y}) collided with you')
                print(" got you ")
                # Handle collision (e.g., increase score, end game, etc.)
            
            if weapon.get_rect().colliderect(ghost.get_rect()):
                # print(f'Ghost at ({ghost.pos_x}, {ghost.pos_y}) was hit by your weapon')
                print(" ouch that hurt ")
             
                # Handle collision (e.g., increase score, end game, etc.)

def deploy_ghosts(char, map, wpn, ghost):
    ghost.update_position(char, map)
    ghost.check_collisions(char, wpn)
    