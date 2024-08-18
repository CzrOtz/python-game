# power_ups.py
import pygame
import random

class PowerUp:
    def __init__(self, config, map_instance):
        self.map_instance = map_instance
        self.pos_x = random.randint(0, map_instance.map_width - 50)
        self.pos_y = random.randint(0, map_instance.map_height - 50)
        self.scale = config["scale"]
        self.type = random.choice(["gray", "green", "red", "blue"])

        # Load and scale the appropriate bottle image
        if self.type == "gray":
            self.sprite = pygame.image.load(config["gray_bottle"]).convert_alpha()
        elif self.type == "green":
            self.sprite = pygame.image.load(config["green_bottle"]).convert_alpha()
        elif self.type == "red":
            self.sprite = pygame.image.load(config["red_bottle"]).convert_alpha()
        elif self.type == "blue":
            self.sprite = pygame.image.load(config["blue_bottle"]).convert_alpha()

        self.sprite = pygame.transform.scale(
            self.sprite,
            (int(self.sprite.get_width() * self.scale),
             int(self.sprite.get_height() * self.scale))
        )

        self.mask = pygame.mask.from_surface(self.sprite)
        self.config = config  # Store the configuration
        self.spawn_time = pygame.time.get_ticks()  # Record the time when the power-up is spawned

    def display(self, screen, offset_x, offset_y):
        screen.blit(self.sprite, (self.pos_x - offset_x, self.pos_y - offset_y))

    def get_mask(self):
        return self.mask

    def get_mask_offset(self):
        return int(self.pos_x), int(self.pos_y)

    def apply_effect(self, hero, weapon):
        if self.type == "gray":
            weapon.attack_speed += self.config["gray_bottle_attack_speed_increase"]
            print("Attack speed increased to", weapon.attack_speed)
        elif self.type == "green":
            hero.speed += self.config["green_bottle_speed_increase"]
            print("Speed increased to", hero.speed)
        elif self.type == "red":
            weapon.damage += self.config["red_bottle_damage_increase"]
            print("Damage increased to", weapon.damage)
        elif self.type == "blue":
            hero.health += self.config["blue_bottle_health_increase"]
            print("Health increased to", hero.health)




class PowerUpManager:
    def __init__(self, config, map_instance, max_power_ups=2):
        self.power_ups = []
        self.max_power_ups = max_power_ups
        self.spawn_interval = random.randint(5000, 15000)  # Random interval between 5 and 15 seconds
        self.last_spawn_time = pygame.time.get_ticks()
        self.map_instance = map_instance
        self.config = config
        self.power_up_lifespan = config["power_up_lifespan"]  # Power-ups stay on screen for 10 seconds (10,000 ms)

    def spawn_power_up(self):
        """Spawn a new power-up if under the limit."""
        if len(self.power_ups) < self.max_power_ups:
            new_power_up = PowerUp(self.config, self.map_instance)
            self.power_ups.append(new_power_up)

    def update(self):
        """Update the power-ups (e.g., spawn new ones if needed)."""
        current_time = pygame.time.get_ticks()

        # Remove power-ups that have exceeded their lifespan
        self.power_ups = [
            power_up for power_up in self.power_ups 
            if current_time - power_up.spawn_time < self.power_up_lifespan
        ]

        # Spawn new power-ups if needed
        if current_time - self.last_spawn_time > self.spawn_interval:
            self.spawn_power_up()
            self.last_spawn_time = current_time
            self.spawn_interval = random.randint(5000, 15000)  # Set new random spawn interval

    def display(self, screen, offset_x, offset_y):
        """Display all active power-ups."""
        for power_up in self.power_ups:
            power_up.display(screen, offset_x, offset_y)

    def check_collisions(self, hero, weapon):
        """Check if the hero collides with any power-ups."""
        hero_mask = hero.get_mask()
        hero_mask_offset = hero.get_mask_offset()
    
        for power_up in self.power_ups:
            power_up_mask = power_up.get_mask()
            power_up_mask_offset = power_up.get_mask_offset()

            # Check for overlap between the hero and power-up masks
            if hero_mask.overlap(power_up_mask, (power_up_mask_offset[0] - hero_mask_offset[0], power_up_mask_offset[1] - hero_mask_offset[1])):
                power_up.apply_effect(hero, weapon)
                self.power_ups.remove(power_up)




    


        
        