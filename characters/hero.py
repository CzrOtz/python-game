import pygame

class Hero:
    def __init__(self, config):
        self.pos_x = config["pos_x"]
        self.pos_y = config["pos_y"]
        self.speed = config["speed"]
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.scale = config["scale"]
        self.config = config
        # Load the sprite directly from the PNG file
        self.sprite = pygame.image.load(config["sprite_path"]).convert_alpha()
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.sprite = pygame.transform.scale(self.sprite, (self.width * self.scale, self.height * self.scale))

    def display(self, screen, offset_x, offset_y):
        screen.blit(self.sprite, (self.pos_x - offset_x, self.pos_y - offset_y))

    def move_up(self):
        self.pos_y -= self.speed

    def move_down(self):
        self.pos_y += self.speed

    def move_right(self):
        self.pos_x += self.speed

    def move_left(self):
        self.pos_x -= self.speed
    
    def positionInTiles(self):
        # When you do anything that is self., you're accessing the member variable that was passed to the class as a parameter
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

        #add or is past the border of the screen 
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

    def display_position(self):
        print(f"Hero position: {self.pos_x}, {self.pos_y}")







