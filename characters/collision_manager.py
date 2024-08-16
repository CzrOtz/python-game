import pygame

class CollisionManager:
    def __init__(self, navbar):
        self.navbar = navbar

    def check_hero_ghost_collisions(self, hero, ghosts):
        """Check and handle collisions between the hero and ghosts."""
        hero_mask = hero.get_mask()
        hero_mask_offset = hero.get_mask_offset()

        for ghost in ghosts:
            ghost_mask = ghost.get_mask()
            ghost_mask_offset = ghost.get_mask_offset()

            if hero_mask.overlap(ghost_mask, (ghost_mask_offset[0] - hero_mask_offset[0], ghost_mask_offset[1] - hero_mask_offset[1])):
                hero.health -= ghost.attack_power
                self.navbar.hero_health = hero.health
                hero.trigger_hurt_effect()

    def check_weapon_ghost_collisions(self, weapon, ghosts):
        """Check and handle collisions between the weapon and ghosts."""
        weapon_mask = weapon.get_mask()
        weapon_mask_offset = weapon.get_mask_offset()

        for ghost in ghosts:
            ghost_mask = ghost.get_mask()
            ghost_mask_offset = ghost.get_mask_offset()

            if weapon_mask.overlap(ghost_mask, (ghost_mask_offset[0] - weapon_mask_offset[0], ghost_mask_offset[1] - weapon_mask_offset[1])) and weapon.attack:
                if not ghost.hit_registered:
                    ghost.reduce_health(weapon)
                    ghost.hit_sound.play()
                    ghost.show_hit_marker()
                    ghost.hit_ammount += 1
                    ghost.hit_registered = True

                if ghost.health <= 0:
                    ghost.gone_sound.play()
                    self.navbar.kill_count += 1
                    ghosts.remove(ghost)
                    self.navbar.enemies_on_screen -= 1

            if not weapon_mask.overlap(ghost_mask, (ghost_mask_offset[0] - weapon_mask_offset[0], ghost_mask_offset[1] - weapon_mask_offset[1])):
                ghost.reset_hit_status()
