import pygame


class Enemy:

    def __init__(self, config):
        self.pos_x = config["pos_x"]
        self.pos_y = config["pos_y"]
        self.speed = config["speed"]
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

        #first is first, loading the sprite

    """the y axis has to subtract offset_y to stay in the same place"""
    """the x axis has to subract offset_x to stay in the same place"""
    def display(self, screen, map):
        screen.blit(self.sprite, (self.pos_x - map.offset_x , self.pos_y - map.offset_y))
    
    def move_up(self):
        self.pos_y -= self.speed
    
    def move_down(self):
        self.pos_y += self.speed

    def move_right(self):
        self.pos_x += self.speed
    
    def move_left(self):
        self.pos_x -= self.speed

    """
    doesnt need movement flags because
    its position is being updated every frame by an algorithm
    """

    """this algorithm will take hero as a parameter"""

    def master_movement(self, hero):
        
        if hero.pos_x > self.pos_x:
            self.move_right() 
        
        if hero.pos_x < self.pos_x:
            self.move_left()
        
        if hero.pos_y > self.pos_y:
            self.move_down()
        
        if hero.pos_y < self.pos_y:
            self.move_up()
        
    
    def inspect(self, hero, map):
        print("Enemy position: x =", self.pos_x, "y =", self.pos_y)
        print("")
        print("Hero position: x =", hero.pos_x, "y =", hero.pos_y)
        print("")
        print("Offset position: x =", map.offset_x, "y =", map.offset_y)


        

    def get_rect(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.width * self.scale, self.height * self.scale)
        