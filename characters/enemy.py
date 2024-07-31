import pygame

#tile_0108.png

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

        


        