import pygame
import random
import time

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

        # Scale the sprite before creating the mask
        self.sprite = pygame.transform.scale(self.sprite, (int(self.width * self.scale), int(self.height * self.scale)))

        # Update width and height after scaling
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

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

    def draw_mask(self, screen, map):
        """
        Draw the ghost's mask as a semi-transparent red overlay on the screen.
        The `map` parameter is used to adjust for the map offset.
        """
        # Create a semi-transparent red surface with the same size as the ghost's sprite
        mask_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        mask_surface.fill((255, 0, 0, 100))  # Red color with alpha = 100 for transparency
    
        # Calculate the position to draw the mask, considering the map offset
        pos_x = self.pos_x - map.offset_x
        pos_y = self.pos_y - map.offset_y
    
        # Blit the red surface onto the screen at the correct position
        screen.blit(mask_surface, (pos_x, pos_y))


class Ghost(Enemy):
    def __init__(self, config):
        super().__init__(config)
        self.r_number_min = config["r_number_min"]
        self.r_number_max = config["r_number_max"]
        self.braking_distance = config["braking_distance"]
        self.speed_modified = False  # Track if speed has been modified
        self.health = config["health"]

        # Load the sound file for when the ghost is hit
        self.hit_sound = pygame.mixer.Sound(config["hit_by_weapon"])
        self.spawn_sound = pygame.mixer.Sound(config["spawn_sound"])
        self.gone_sound = pygame.mixer.Sound(config["gone_sound"])
        self.hit_ammount = 0
        self.hit_registered = False

        # Hit marker attributes
        self.hit_marker_duration = 0.1  # duration in seconds
        self.hit_marker_size = 20  # size of the hit marker
        self.hit_marker_color = (255, 0, 0)  # red color
        self.hit_marker_time = 0  # time when the hit marker should disappear

        

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
    
    def play_hit_sound(self):
        """Play the sound when the ghost is hit."""
        self.hit_sound.play()
    
    def reduce_health(self, ghost, weapon):
        print("reducing health")
        self.health -= weapon.damage
        self.show_hit_marker()

    def show_hit_marker(self):
        """Trigger the hit marker display."""
        self.hit_marker_time = time.time() + self.hit_marker_duration

    def draw_hit_marker(self, screen, map):
        """Draw the hit marker if it's within the display time."""
        if time.time() < self.hit_marker_time:
            marker_rect = pygame.Rect(
                self.pos_x - map.offset_x + self.width // 2 - self.hit_marker_size // 2,
                self.pos_y - map.offset_y + self.height // 2 - self.hit_marker_size // 2,
                self.hit_marker_size,
                self.hit_marker_size
            )
            pygame.draw.rect(screen, self.hit_marker_color, marker_rect)

    def reset_hit_status(self):
        """Reset the hit status of the ghost."""
        self.hit_registered = False

    
        

            
            

    
    
        

    
    

    
    
    
    
        
        

            



