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

    def _calculate_angle(self, x1, y1, x2, y2):
        print(f"x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}")
        print("pointer_x: ", self.pointer_x, "pointer_y: ", self.pointer_y)
        return math.atan2(y2 - y1, x2 - x1)
    
    def display(self, screen, offset_x, offset_y):
        # Update pointer position
        self.pointer_x, self.pointer_y = pygame.mouse.get_pos()
        
        # Calculate angle between hero and cursor
        angle = self._calculate_angle(self.pos_x - offset_x, self.pos_y - offset_y, self.pointer_x, self.pointer_y)

        # Adjust angle to correct for the 90 degrees offset
        angle -= math.pi / 2  # Subtract 90 degrees (pi/2 radians)
        angle += math.pi

        # Rotate weapon sprite
        rotated_sprite = pygame.transform.rotate(self.sprite, -math.degrees(angle))

        # Calculate new rect position to keep the sprite centered
        new_rect = rotated_sprite.get_rect(center=(self.pos_x - offset_x, self.pos_y - offset_y))

        # Blit the rotated weapon sprite
        screen.blit(rotated_sprite, new_rect.topleft)
        screen.blit(self.pointer_image, (self.pointer_x, self.pointer_y))

    def update_position(self, hero):
        """This method keeps the weapon attached to the hero"""
        if not self.attack:
            self.pos_x = hero.pos_x
            self.pos_y = hero.pos_y

        # Update pointer position in case it changed
        self.pointer_x, self.pointer_y = pygame.mouse.get_pos()

    def launch_attack(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.attack = True
                print("Attack launched")
    
    def fire(self, hero):
        if self.attack:
            self.pos_y -= self.attack_speed
        
        if self.pos_y < 0:
            self.attack = False
            self.pos_y = hero.pos_y
            print("Attack ended")

    def get_rect(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)



    


    

    
