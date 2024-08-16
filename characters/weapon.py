#weapon.py
import pygame
import math

"""
Weapon oberves Hero -> no Weapon calls in Hero class

"""

import pygame
import math

class Weapon:
    def __init__(self, config, hero):
        self.hero = hero
        self.pos_x = hero.pos_x
        self.pos_y = hero.pos_y
        self.attack_speed = config["speed"]
        self.scale = config["scale"]
        self.damage = config["damage"]
        self.attack = False
        self.hit_by_weapon = False
        self.angle = 0

        # Load and scale the weapon sprite (Original Sprite)
        self.original_sprite = pygame.image.load(config["sprite_path"]).convert_alpha()

        self.original_sprite = pygame.transform.scale(
            self.original_sprite, 
            (int(self.original_sprite.get_width() * self.scale), 
            int(self.original_sprite.get_height() * self.scale))
        )

        self.width = self.original_sprite.get_width()
        self.height = self.original_sprite.get_height()

        # Load and scale the pointer image
        self.pointer_image = pygame.image.load(config["pointer_sp"]).convert_alpha()
        
        self.pointer_image = pygame.transform.scale(
            self.pointer_image, 
            (int(self.pointer_image.get_width() * self.scale), 
            int(self.pointer_image.get_height() * self.scale))
        )

        # Create the initial mask for pixel-perfect collision detection
        self.mask = pygame.mask.from_surface(self.original_sprite)

        # Initialize pointer position
        self.pointer_x, self.pointer_y = pygame.mouse.get_pos()

        # Initialize direction vector
        self.dir_x = 0
        self.dir_y = 0

        self.sound = pygame.mixer.Sound(config["sound"])
        self.collision_sound = pygame.mixer.Sound(config["collision_sound"])

    def _calculate_angle(self, x1, y1, x2, y2):
        return math.atan2(y2 - y1, x2 - x1)

    def _calculate_direction(self, x1, y1, x2, y2):
        angle = self._calculate_angle(x1, y1, x2, y2)
        return math.cos(angle), math.sin(angle)

    def display(self, screen, off_x, off_y):
        """Display the weapon on the screen."""
        if not self.attack:
            pointer_x_corrected = self.pointer_x + off_x
            pointer_y_corrected = self.pointer_y + off_y
            self.angle = self._calculate_angle(self.pos_x, self.pos_y, pointer_x_corrected, pointer_y_corrected)

        # Rotate the weapon sprite
        rotated_sprite = pygame.transform.rotate(self.original_sprite, -math.degrees(self.angle) - 90)
        new_rect = rotated_sprite.get_rect(center=(self.pos_x, self.pos_y))
        screen.blit(rotated_sprite, (new_rect.x - off_x, new_rect.y - off_y))

        # Update the mask after rotation
        self.mask = pygame.mask.from_surface(rotated_sprite)

        # Center the pointer image with the tip of the cursor
        pointer_center_x = self.pointer_x - self.pointer_image.get_width() // 2
        pointer_center_y = self.pointer_y - self.pointer_image.get_height() // 2
        screen.blit(self.pointer_image, (pointer_center_x, pointer_center_y))

    def update_position(self, hero):
        if not self.attack:
            self.pos_x = hero.pos_x
            self.pos_y = hero.pos_y
        self.pointer_x, self.pointer_y = pygame.mouse.get_pos()

    def launch_attack(self, event, off_x, off_y):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not self.attack:
                self.sound.play()
                self.attack = True
                pointer_x_corrected = self.pointer_x + off_x
                pointer_y_corrected = self.pointer_y + off_y
                self.dir_x, self.dir_y = self._calculate_direction(self.pos_x, self.pos_y, pointer_x_corrected, pointer_y_corrected)

    def fire(self, map_width, map_height, map):
        if self.attack:
            self.pos_x += self.dir_x * self.attack_speed
            self.pos_y += self.dir_y * self.attack_speed

        if self.pos_y < 0 or self.pos_x < 0 or self.pos_y > map_height or self.pos_x > map_width:
            self.reset()

        if map.collided_with(self):
            self.collision_sound.play()
            self.reset()

    def reset(self):
        """Reset weapon position and state."""
        self.attack = False
        self.pos_x = self.hero.pos_x
        self.pos_y = self.hero.pos_y

    def get_mask(self):
        return self.mask

    def get_mask_offset(self):
        return int(self.pos_x), int(self.pos_y)

    def get_rect(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)








    

    







    

    







    


    

    
