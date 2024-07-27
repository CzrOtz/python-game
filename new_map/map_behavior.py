import pygame
import pytmx

#this class renders a map
#applies a mask to the map to detect collisions
#no need to change this class
class Map:
    def __init__(self, config):
        self.config = config
        self.tmx_data = pytmx.load_pygame(config["tilemap_path"], pixelalpha=config["pixelalpha"])
        self.map_width = self.tmx_data.width * self.tmx_data.tilewidth * config["scale"]
        self.map_height = self.tmx_data.height * self.tmx_data.tileheight * config["scale"]
        self.offset_x = 0
        self.offset_y = 0
        self.scale = config["scale"]

        # Initialize collision surface and mask
        self.collision_surface = pygame.Surface((self.map_width, self.map_height), pygame.SRCALPHA)
        self.collision_mask = None
        self._create_collision_mask()

    def _create_collision_mask(self):
        """Create a collision surface and mask based on the map's objects"""
        self.collision_surface.fill((0, 0, 0, 0))  # Clear surface

        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledObjectGroup) and layer.name == self.config["layer_name"]:
                for obj in layer:
                    if obj.type == self.config["object_type"]:
                        if hasattr(obj, 'polygon'):
                            polygon_points = [(obj.x + p[0], obj.y + p[1]) for p in obj.polygon]
                            polygon_points_scaled = [(x * self.scale, y * self.scale) for x, y in polygon_points]
                            pygame.draw.polygon(self.collision_surface, (255, 0, 0, 255), polygon_points_scaled)
                        elif hasattr(obj, 'polyline'):
                            polyline_points = [(obj.x + p[0], obj.y + p[1]) for p in obj.polyline]
                            polyline_points_scaled = [(x * self.scale, y * self.scale) for x, y in polyline_points]
                            pygame.draw.lines(self.collision_surface, (255, 0, 0, 255), False, polyline_points_scaled, 2)
                        else:
                            tile_rect = pygame.Rect(
                                obj.x * self.scale,
                                obj.y * self.scale,
                                obj.width * self.scale,
                                obj.height * self.scale
                            )
                            pygame.draw.rect(self.collision_surface, (255, 0, 0, 255), tile_rect)

        self.collision_mask = pygame.mask.from_surface(self.collision_surface)

    def draw(self):
        screen_width, screen_height = self.config["screen_width"], self.config["screen_height"]
        start_x = max(0, self.offset_x // (self.tmx_data.tilewidth * self.scale))
        start_y = max(0, self.offset_y // (self.tmx_data.tileheight * self.scale))
        end_x = min(self.tmx_data.width, (self.offset_x + screen_width) // (self.tmx_data.tilewidth * self.scale) + 1)
        end_y = min(self.tmx_data.height, (self.offset_y + screen_height) // (self.tmx_data.tileheight * self.scale) + 1)

        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x in range(start_x, end_x):
                    for y in range(start_y, end_y):
                        gid = layer.data[y][x]
                        if gid:
                            tile = self.tmx_data.get_tile_image_by_gid(gid)
                            if tile:
                                scaled_tile = pygame.transform.scale(tile, (self.tmx_data.tilewidth * self.scale, self.tmx_data.tileheight * self.scale))
                                self.config["screen"].blit(scaled_tile, (x * self.tmx_data.tilewidth * self.scale - self.offset_x, y * self.tmx_data.tileheight * self.scale - self.offset_y))

    def update_offset(self, hero_pos_x, hero_pos_y):
        screen_width, screen_height = self.config["screen_width"], self.config["screen_height"]
        self.offset_x = max(0, min(hero_pos_x - screen_width // 2, self.map_width - screen_width))
        self.offset_y = max(0, min(hero_pos_y - screen_height // 2, self.map_height - screen_height))

    def collided_with(self, hero):
        hero_rect = hero.get_rect()

        # Create a mask for the hero sprite
        hero_mask = pygame.mask.from_surface(hero.sprite)
        offset = (hero_rect.x, hero_rect.y)

        # Check for overlap between the hero mask and the collision mask
        overlap = self.collision_mask.overlap(hero_mask, offset)
        # print(f"Collision check at offset: {offset}, overlap: {overlap}")

        if overlap:
            # print("Collision detected: True")
            return True
        else:
            # print("No collision detected: False")
            return False











    
                

       

    
       
