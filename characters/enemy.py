import pygame
import random

"""
These classes dictate the behavior of the individual enemies in the game
"""

class Enemy:
    def __init__(self, config):
        self.pos_x = config["pos_x"]
        self.pos_y = config["pos_y"]
        self.speed = config["speed"]
        self.original_speed = self.speed  # Store the original speed
        self.scale = config["scale"]
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        # Load the sprite directly from the PNG file
        self.sprite = pygame.image.load(config["sprite_path"]).convert_alpha()
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.sprite = pygame.transform.scale(self.sprite, (self.width * self.scale, self.height * self.scale))

        # Create a mask for pixel-perfect collision detection
        self.mask = pygame.mask.from_surface(self.sprite)

    def display(self, screen, map):
        screen.blit(self.sprite, (self.pos_x - map.offset_x, self.pos_y - map.offset_y))
    
    def move_up(self):
        self.pos_y -= self.speed
    
    def move_down(self):
        self.pos_y += self.speed

    def move_right(self):
        self.pos_x += self.speed
    
    def move_left(self):
        self.pos_x -= self.speed

    def get_mask(self):
        """
        Return the mask of the enemy for pixel-perfect collision detection.
        """
        return self.mask

    def get_mask_offset(self):
        """
        Return the position offset of the mask to use in collision detection.
        """
        return (int(self.pos_x), int(self.pos_y))

class Ghost(Enemy):
    def __init__(self, config):
        super().__init__(config)
        self.r_number_min = config["r_number_min"]
        self.r_number_max = config["r_number_max"]
        self.braking_distance = config["braking_distance"]
        self.speed_modified = False  # Track if speed has been modified
        self.health = config["health"]

    def master_movement(self, hero):
        # Calculate the distance between the ghost and the hero
        distance = ((hero.pos_x - self.pos_x) ** 2 + (hero.pos_y - self.pos_y) ** 2) ** 0.5

        if distance < self.braking_distance:
            self._restore_speed()
        else:
            self._modify_speed()

        if hero.pos_x > self.pos_x:
            self.move_right()
        elif hero.pos_x < self.pos_x:
            self.move_left()
        
        if hero.pos_y > self.pos_y:
            self.move_down()
        elif hero.pos_y < self.pos_y:
            self.move_up()

    def _modify_speed(self):
        if not self.speed_modified:  # Only modify speed if it hasn't been modified yet
            lottery_number = random.randint(self.r_number_min, self.r_number_max)
            number_drawn = random.randint(self.r_number_min, self.r_number_max)

            if lottery_number == number_drawn:
                self.speed = lottery_number
                self.speed_modified = True

    def _restore_speed(self):
        self.speed = self.original_speed
        self.speed_modified = False

    
    
    
    
        
        

            



