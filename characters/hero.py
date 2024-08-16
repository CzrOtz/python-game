#hero.py
import pygame
import time

"""
Hearo in ghost Ghost manager
-> collision detection using masks
-> ghost.master_movement(hero)
-> mask overlap
-> hero.health -= 0.5

Hero in enemy
-> hero.pos_x , hero.pos_y

Hero in Weapon
-> hero.pos_x, hero.pos_y

Hero in game
-> hero
-> weapon
-> navbar




"""

class Hero:
    def __init__(self, config):
        self.pos_x = config["pos_x"] * config["scale"]
        self.pos_y = config["pos_y"] * config["scale"]
        self.speed = config["speed"] * config["scale"]
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.scale = config["scale"]
        self.config = config
        self.health = config["health"]

        # Load the sprite directly from the PNG file
        self.sprite = pygame.image.load(config["sprite_path"]).convert_alpha()
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.sprite = pygame.transform.scale(self.sprite, (self.width * self.scale, self.height * self.scale))

        # Create a mask for pixel-perfect collision detection
        self.mask = pygame.mask.from_surface(self.sprite)

        # Hurt effect attributes
        self.hurt_time = 0  # Time when the hero was last hurt
        self.hurt_duration = 0.1  # Duration of the hurt effect in seconds

    def display(self, screen, offset_x, offset_y):
        screen.blit(self.sprite, (self.pos_x - offset_x, self.pos_y - offset_y))
        self.draw_hurt_mask(screen, offset_x, offset_y)

    def move_up(self):
        self.pos_y -= self.speed

    def move_down(self):
        self.pos_y += self.speed

    def move_right(self):
        self.pos_x += self.speed

    def move_left(self):
        self.pos_x -= self.speed
    
    def positionInTiles(self):
        tile_x = (self.pos_x // (16 * self.scale))
        tile_y = (self.pos_y // (16 * self.scale))
        print(f"Hero is at tile coordinates (x: {tile_x}, y: {tile_y})")

    def x_positionInTiles(self):
        return (self.pos_x // (16 * self.scale))
    
    def y_positionInTiles(self):
        return (self.pos_y // (16 * self.scale))
    
    def master_movement(self, map_instance):
        initial_pos_x = self.pos_x
        initial_pos_y = self.pos_y

        if self.moving_left:
            self.move_left()
        if self.moving_right:
            self.move_right()
        if self.moving_up:
            self.move_up()
        if self.moving_down:
            self.move_down()

        if map_instance.collided_with(self):
            self.pos_x = initial_pos_x
            self.pos_y = initial_pos_y

    def movement_flags(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.moving_left = True
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.moving_right = True
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                self.moving_up = True
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.moving_left = False
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.moving_right = False
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                self.moving_up = False
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.moving_down = False

    def get_rect(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

    def get_mask(self):
        """Return the mask of the hero for pixel-perfect collision detection."""
        return self.mask

    def get_mask_offset(self):
        """Return the position offset of the mask to use in collision detection."""
        return int(self.pos_x), int(self.pos_y)

    def draw_mask(self, screen, offset_x, offset_y):
        """Draw the mask on the screen for debugging purposes."""
        mask_surface = self.mask.to_surface(setcolor=(255, 0, 0, 128), unsetcolor=(0, 0, 0, 0))
        screen.blit(mask_surface, (self.pos_x - offset_x, self.pos_y - offset_y))

    def draw_hurt_mask(self, screen, offset_x, offset_y):
        """Draw the hero's mask briefly when hurt."""
        current_time = time.time()
        if current_time - self.hurt_time < self.hurt_duration:
            mask_surface = self.mask.to_surface(setcolor=(255, 0, 0, 128), unsetcolor=(0, 0, 0, 0))
            screen.blit(mask_surface, (self.pos_x - offset_x, self.pos_y - offset_y))

    def trigger_hurt_effect(self):
        """Trigger the hurt effect."""
        self.hurt_time = time.time()

    def display_position(self):
        print(f"Hero position: {self.pos_x}, {self.pos_y}")
    
    def inspect(self):
        print("----- HERO INSPECTION -----")
        print(" ")
        print(" ")
        print(" ------ Hero specs ------  ")
        print(f"Speed: {self.speed}")
        print(f"Scale: {self.scale}")
        print(f"Hero Sprite Dimensions (width x height): ({self.width} x {self.height})")
        print("-------------------------")
        print(" ")
        print(" ")
        print(" ------ Hero Position ------  ")
        print(f"Hero Position (pos_x, pos_y): ({self.pos_x}, {self.pos_y})")
        print(f'Hero Position in tiles (x, y): ({self.x_positionInTiles()}, {self.y_positionInTiles()})')
        print(f'Hero scale (scale): {self.scale}')
        print("-------------------------")
    
        print("----- Hero State --------")
        print(f"Moving Left: {self.moving_left}")
        print(f"Moving Right: {self.moving_right}")
        print(f"Moving Up: {self.moving_up}")
        print(f"Moving Down: {self.moving_down}")
        print(" ----------------------")
        print(" ")
        print(" ")

def deploy_hero(char, map, screen, off_x, off_y):
    char.master_movement(map)
    char.display(screen, off_x, off_y)
    # char.draw_mask(screen, off_x, off_y)  # Optional: Draw the mask for debugging

   








