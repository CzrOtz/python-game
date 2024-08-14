import pygame
from characters.enemy import Ghost
from config import generate_ghost_config

"""variable set to true if the ghost is hit by the weapon"""
"""this will only allow the ghost to be hit once"""

class GhostManager:
    def __init__(self, config):
        self.ghosts = []
        self.screen = config["screen"]
        self.scale = config["scale"]
        self.spawn_rate = config["spawn_rate"]
        self.add_ghost_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.add_ghost_event, self.spawn_rate)  # Add a new ghost every `spawn_rate` milliseconds
        self.initial_ghost_quantity = config["initial_ghost_quantity"]
        self._generate_initial_ghosts()

    """this method generates the initial ghosts"""
    def _generate_initial_ghosts(self):
        for _ in range(self.initial_ghost_quantity):
            self.ghosts.append(Ghost(generate_ghost_config()))

    """this method applies the master movement method to each ghost in the list"""
    def update_position(self, hero, game_map):
        for ghost in self.ghosts:
            ghost.master_movement(hero)
            ghost.display(self.screen, game_map)
            ghost.draw_hit_marker(self.screen, game_map)
            

    """this method adds a new ghost to the list"""
    def add_new_ghost(self):
        new_ghost_config = generate_ghost_config()
        self.ghosts.append(Ghost(new_ghost_config))

    

    def check_collisions(self, hero, weapon):
        hero_mask = hero.get_mask()
        hero_mask_offset = hero.get_mask_offset()

        weapon_mask = weapon.get_mask()
        weapon_mask_offset = weapon.get_mask_offset()

        for ghost in self.ghosts:
            ghost_mask = ghost.get_mask()
            ghost_mask_offset = ghost.get_mask_offset()

            # Check collision between hero and ghost
            if hero_mask.overlap(ghost_mask, (ghost_mask_offset[0] - hero_mask_offset[0], ghost_mask_offset[1] - hero_mask_offset[1])):
                print(" got you ")

            # Check collision between weapon and ghost
            if weapon_mask.overlap(ghost_mask, (ghost_mask_offset[0] - weapon_mask_offset[0], ghost_mask_offset[1] - weapon_mask_offset[1])) and weapon.attack:
                if not ghost.hit_registered:
                    ghost.reduce_health(ghost, weapon)
                    ghost.hit_sound.play()
                    ghost.show_hit_marker()
                    ghost.hit_ammount += 1
                    ghost.hit_registered = True  # Mark ghost as hit
                    print(f'ammount of hits: {ghost.hit_ammount}')
                    print(f'ghost health: {ghost.health}')
                    

                if ghost.health <= 0:
                    ghost.show_hit_marker()
                    self.ghosts.remove(ghost)
                    

        # Reset hit status if the projectile is no longer in contact
            if not weapon_mask.overlap(ghost_mask, (ghost_mask_offset[0] - weapon_mask_offset[0], ghost_mask_offset[1] - weapon_mask_offset[1])):
                ghost.reset_hit_status()
                
                
    def inspect(self):
        """Prints out detailed information about each ghost in the list."""
        print("----- Ghost List Detailed Inspection -----")
        for idx, ghost in enumerate(self.ghosts):
            print(f"Ghost {idx + 1}:")
            print(f"  - Position: ({ghost.pos_x}, {ghost.pos_y})")
            print(f"  - Health: {ghost.health}")
            print(f"  - Speed: {ghost.speed}")
            print(f"  - Scale: {ghost.scale}")
            print(f"  - Sprite Dimensions: (Width: {ghost.width * ghost.scale}, Height: {ghost.height * ghost.scale})")
            print(f"  - Braking Distance: {ghost.braking_distance}")
            print(f"  - Random Number Range: ({ghost.r_number_min}, {ghost.r_number_max})")
            print(f"  - Speed Modified: {ghost.speed_modified}")
            print(f"  - Original Speed: {ghost.original_speed}")
            print("----------------------")
        print("----- END OF INSPECTION -----\n")
    
    def draw_all_masks(self, game_map):
        """
        Draws the collision mask of each ghost as a semi-transparent red overlay for debugging.
        """
        # print("every ghost has a mask")
        for ghost in self.ghosts:
            ghost.draw_mask(self.screen, game_map)
            

def deploy_ghosts(char, map, wpn, ghost_manager):
    ghost_manager.update_position(char, map)
    ghost_manager.check_collisions(char, wpn)
    # ghost_manager.draw_all_masks(map)
    