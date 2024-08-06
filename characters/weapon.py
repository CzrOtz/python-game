import pygame


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
        self.sprite = pygame.image.load(config["sprite_path"]).convert_alpha()
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

        self.pointer = pygame.mouse.get_pos()
        self.pointer_x = self.pointer[0]
        self.pointer_y = self.pointer[1]
        self.pointer_image = pygame.image.load(config["pointer_sp"]).convert_alpha()

    def display(self, screen, offset_x, offset_y):
        screen.blit(self.sprite, (self.pos_x - offset_x, self.pos_y - offset_y))
        screen.blit(self.pointer_image, (self.pointer_x, self.pointer_y))
    
    
    def update_position(self, hero):
        
        if self.attack == False:
            self.pos_x = hero.pos_x
            self.pos_y = hero.pos_y
        

        self.pointer_x = pygame.mouse.get_pos()[0]
        self.pointer_y = pygame.mouse.get_pos()[1]
    
    
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
        return pygame.Rect(self.pos_x, self.pos_y, self.width * self.scale, self.height * self.scale)


    

    
