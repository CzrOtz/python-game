import pygame
import math

"""This class handles a long-range weapon that the hero can use"""

class Weapon:
    def __init__(self, config, hero):
        # Initialize the weapon's position relative to the hero's initial position
        self.pos_x = hero.pos_x
        self.pos_y = hero.pos_y

        # Weapon attributes from config
        self.attack_speed = config["speed"]
        self.scale = config["scale"]
        self.damage = config["damage"]

        # Weapon state flags
        self.attack = False
        self.angle = 0  # Initialize angle

        # Load and scale the weapon sprite
        self.sprite = pygame.image.load(config["sprite_path"]).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (int(self.sprite.get_width() * self.scale), int(self.sprite.get_height() * self.scale)))
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

        # Create a mask for pixel-perfect collision
        self.mask = pygame.mask.from_surface(self.sprite)

        # Load and scale the pointer image
        self.pointer_image = pygame.image.load(config["pointer_sp"]).convert_alpha()
        self.pointer_image = pygame.transform.scale(self.pointer_image, (int(self.pointer_image.get_width() * self.scale), int(self.pointer_image.get_height() * self.scale)))

        # Initialize pointer position
        self.pointer_x, self.pointer_y = pygame.mouse.get_pos()

        # Initialize direction vector
        self.dir_x = 0
        self.dir_y = 0

    def _calculate_angle(self, x1, y1, x2, y2):
        return math.atan2(y2 - y1, x2 - x1)

    def _calculate_direction(self, x1, y1, x2, y2):
        angle = self._calculate_angle(x1, y1, x2, y2)
        return math.cos(angle), math.sin(angle)

    def display(self, screen, off_x, off_y):
        """
        Display the weapon on the screen.
        The `off_x` and `off_y` parameters represent the map offsets (game_map.offset_x and game_map.offset_y).
        """
        # Use the stored angle if the attack is in progress
        if not self.attack:
            # Correct the pointer position by the offset
            pointer_x_corrected = self.pointer_x + off_x
            pointer_y_corrected = self.pointer_y + off_y
            self.angle = self._calculate_angle(self.pos_x, self.pos_y, pointer_x_corrected, pointer_y_corrected)
        
        # Rotate weapon sprite
        rotated_sprite = pygame.transform.rotate(self.sprite, -math.degrees(self.angle) - 90)
        new_rect = rotated_sprite.get_rect(center=(self.pos_x - off_x, self.pos_y - off_y))
        screen.blit(rotated_sprite, new_rect.topleft)

        # Center the pointer image with the tip of the cursor
        pointer_center_x = self.pointer_x - self.pointer_image.get_width() // 2
        pointer_center_y = self.pointer_y - self.pointer_image.get_height() // 2
        screen.blit(self.pointer_image, (pointer_center_x, pointer_center_y))

    def update_position(self, hero):
        """
        Update the weapon's position to keep it attached to the hero.
        The weapon's position is updated only when the attack is not in progress.
        """
        if not self.attack:
            self.pos_x = hero.pos_x
            self.pos_y = hero.pos_y

        # Update pointer position in case it changed
        self.pointer_x, self.pointer_y = pygame.mouse.get_pos()

    def launch_attack(self, event, off_x, off_y):
        """
        Trigger the attack when a mouse click is detected.
        The `off_x` and `off_y` parameters represent the map offsets (game_map.offset_x and game_map.offset_y).
        """
        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) and not self.attack:
            self.attack = True
            pointer_x_corrected = self.pointer_x + off_x
            pointer_y_corrected = self.pointer_y + off_y
            self.dir_x, self.dir_y = self._calculate_direction(self.pos_x, self.pos_y, pointer_x_corrected, pointer_y_corrected)

    def fire(self, hero, map_width, map_height, map):
        """
        Move the weapon in the direction of the pointer if an attack is in progress.
        The weapon resets to the hero's position if it goes out of the map's bounds.
        """
        if self.attack:
            # Move the weapon in the direction of the pointer
            self.pos_x += self.dir_x * self.attack_speed
            self.pos_y += self.dir_y * self.attack_speed

        # Check against the full map boundaries, not just screen size
        if (self.pos_y < 0 or self.pos_x < 0 or 
            self.pos_y > map_height or self.pos_x > map_width):
            self.attack = False
            self.pos_x = hero.pos_x
            self.pos_y = hero.pos_y
        
        if map.collided_with(self):
            self.attack = False
            self.pos_x = hero.pos_x
            self.pos_y = hero.pos_y
            print("collision detected with map")

    def get_mask(self):
        """
        Return the mask of the weapon for pixel-perfect collision detection.
        """
        return self.mask

    def get_mask_offset(self):
        """
        Return the position offset of the mask to use in collision detection.
        """
        return (int(self.pos_x), int(self.pos_y))
    
    def get_rect(self):
        """
        Return the weapon's rectangle for collision detection.
        """
        return pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

    def inspect(self):
        """
        Print out detailed information about the weapon's state for debugging purposes.
        """
        print(" ------ weapon travel --------")
        print(f"Scale: {self.scale}")
        print(f"Attack Status: {self.attack}")
        print(f"Weapon Position (pos_x, pos_y): ({self.pos_x}, {self.pos_y})")
        print(f"Pointer Position (pointer_x, pointer_y): ({self.pointer_x}, {self.pointer_y})")
        print(f"Direction Vector (dir_x, dir_y): ({self.dir_x}, {self.dir_y})")
        angle = self._calculate_angle(self.pos_x, self.pos_y, self.pointer_x, self.pointer_y)
        print(f"Calculated Angle (radians): {angle}")
        print(f"Calculated Angle (degrees): {math.degrees(angle)}")
        print("---------------------")
        print("----- END OF INSPECTION -----\n")


    def draw_mask(self, screen, off_x, off_y):
        """
        Draw the weapon's mask as a semi-transparent red overlay on the screen.
        The `off_x` and `off_y` parameters represent the map offsets (game_map.offset_x and game_map.offset_y).
        """
        # Create a red surface with the same size as the weapon's sprite and apply the mask
        red_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        red_surface.fill((0, 0, 255))  
    
        # Blit the mask on the red surface
        red_surface.blit(self.sprite, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    
        # Calculate the position to draw the mask
        pos_x = self.pos_x - off_x
        pos_y = self.pos_y - off_y
    
        # Blit the red surface onto the screen at the correct position
        screen.blit(red_surface, (pos_x, pos_y))

    

    







    

    







    


    

    
