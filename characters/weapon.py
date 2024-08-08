import pygame
import math

class Weapon:
    def __init__(self, config, hero):
        self.pos_x = hero.pos_x
        self.pos_y = hero.pos_y
        self.damage = config["damage"]
        self.range = config["range"]
        self.attack_speed = config["speed"]
        self.attack_cooldown = config["cooldown"]
        self.scale = config["scale"]
        
        self.attack = False
        self.colided = False
        self.out_of_range = False
        self.out_of_map = False

        # Load and scale the weapon sprite
        self.sprite = pygame.image.load(config["sprite_path"]).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (int(self.sprite.get_width() * self.scale), int(self.sprite.get_height() * self.scale)))
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

        # Load and scale the pointer image
        self.pointer_image = pygame.image.load(config["pointer_sp"]).convert_alpha()
        self.pointer_image = pygame.transform.scale(self.pointer_image, (int(self.pointer_image.get_width() * self.scale), int(self.pointer_image.get_height() * self.scale)))
        self.pointer_x, self.pointer_y = pygame.mouse.get_pos()

        # Initialize direction vector
        self.dir_x = 0
        self.dir_y = 0

    def _calculate_angle(self, x1, y1, x2, y2):
        return math.atan2(y2 - y1, x2 - x1)

    def _calculate_direction(self, x1, y1, x2, y2):
        angle = self._calculate_angle(x1, y1, x2, y2)
        return math.cos(angle), math.sin(angle)
    
    def display(self, screen, offset_x, offset_y):
        # Rotate weapon sprite
        rotated_sprite = pygame.transform.rotate(self.sprite, -math.degrees(self._calculate_angle(self.pos_x - offset_x, self.pos_y - offset_y, self.pointer_x, self.pointer_y)) - 90)

        # Calculate new rect position to keep the sprite centered
        new_rect = rotated_sprite.get_rect(center=(self.pos_x - offset_x, self.pos_y - offset_y))

        # Blit the rotated weapon sprite
        screen.blit(rotated_sprite, new_rect.topleft)
        screen.blit(self.pointer_image, (self.pointer_x, self.pointer_y))

    def update_position(self, hero):
        """This method keeps the weapon attached to the hero"""
        if not self.attack:
            # Position of weapon
            self.pos_x = hero.pos_x
            self.pos_y = hero.pos_y

        # Update pointer position in case it changed
        self.pointer_x, self.pointer_y = pygame.mouse.get_pos()

    def launch_attack(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.attack = True
                self.dir_x, self.dir_y = self._calculate_direction(self.pos_x, self.pos_y, self.pointer_x, self.pointer_y)
                print("Attack launched")

    def fire(self, hero):
        if self.attack:
            # Move the weapon in the direction of the pointer
            self.pos_x += self.dir_x * self.attack_speed
            self.pos_y += self.dir_y * self.attack_speed
        
        if self.pos_y < 0 or self.pos_x < 0 or self.pos_y > hero.config["screen_height"] or self.pos_x > hero.config["screen_width"]:
            self.attack = False
            self.pos_x = hero.pos_x
            self.pos_y = hero.pos_y
            print("Attack ended")

    def get_rect(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)



    


    

    
