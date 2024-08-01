import pygame

class Enemy:
    def __init__(self, config):
        self.pos_x = config["pos_x"]
        self.pos_y = config["pos_y"]
        self.speed = config["speed"]
        self.scale = config["scale"]
        self.increment_factor = config["increment"]
        self.speed_limit = config["speed_limit"]
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        # Load the sprite directly from the PNG file
        self.sprite = pygame.image.load(config["sprite_path"]).convert_alpha()
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.sprite = pygame.transform.scale(self.sprite, (self.width * self.scale, self.height * self.scale))

    def display(self, screen, map):
        screen.blit(self.sprite, (self.pos_x - map.offset_x, self.pos_y - map.offset_y))
    
    def move_up(self):
        if self.speed < self.speed_limit:
            self.speed += self.increment_factor

        self.pos_y -= self.speed
    
    def move_down(self):
        if self.speed < self.speed_limit:
            self.speed += self.increment_factor
        self.pos_y += self.speed

    def move_right(self):
        if self.speed < self.speed_limit:
            self.speed += self.increment_factor
        self.pos_x += self.speed
    
    def move_left(self):
        if self.speed < self.speed_limit:
            self.speed += self.increment_factor
        self.pos_x -= self.speed

    def get_rect(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.width * self.scale, self.height * self.scale)

class Ghost(Enemy):
    """need a way to keep the sprites separate"""
    def master_movement(self, hero):
        if hero.pos_x > self.pos_x:
            self.move_right()
        
        if hero.pos_x < self.pos_x:
            self.move_left()
        
        if hero.pos_y > self.pos_y:
            self.move_down()
        
        if hero.pos_y < self.pos_y:
            self.move_up()

class Crab(Enemy):
    def master_movement(self, hero, map_instance):
        initial_pos_x = self.pos_x
        initial_pos_y = self.pos_y

        if hero.pos_x > self.pos_x:
            self.move_right()
        
        if hero.pos_x < self.pos_x:
            self.move_left()
        
        if hero.pos_y > self.pos_y:
            self.move_down()
        
        if hero.pos_y < self.pos_y:
            self.move_up()
        
        if map_instance.collided_with(self):
            self.pos_x = initial_pos_x
            self.pos_y = initial_pos_y

class Soldier(Enemy):
    def master_movement(self, hero, map_instance):
        initial_pos_x = self.pos_x
        initial_pos_y = self.pos_y

        if hero.pos_x > self.pos_x:
            self.move_right()
        
        if hero.pos_x < self.pos_x:
            self.move_left()
        
        if hero.pos_y > self.pos_y:
            self.move_down()
        
        if hero.pos_y < self.pos_y:
            self.move_up()
        
        if map_instance.collided_with(self):
            self.pos_x = initial_pos_x
            self.pos_y = initial_pos_y
