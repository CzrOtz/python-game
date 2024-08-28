#map behavior
import pygame
import pytmx

"""
when creating the objects on tiled, assure that the beggining of the object is in the top lefthad corner of the object
if not, youll see the object being drawn in the wrong place
"""

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
                            polygon_points = [(obj.x * self.scale + p[0] * self.scale, obj.y * self.scale + p[1] * self.scale) for p in obj.polygon]
                            pygame.draw.polygon(self.collision_surface, (255, 0, 0, 255), polygon_points)
                        elif hasattr(obj, 'polyline'):
                            polyline_points = [(obj.x * self.scale + p[0] * self.scale, obj.y * self.scale + p[1] * self.scale) for p in obj.polyline]
                            pygame.draw.lines(self.collision_surface, (255, 0, 0, 255), False, polyline_points, 2)
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
                                draw_pos = (x * self.tmx_data.tilewidth * self.scale - self.offset_x, y * self.tmx_data.tileheight * self.scale - self.offset_y)
                                self.config["screen"].blit(scaled_tile, draw_pos)

    def update_offset(self, hero_pos_x, hero_pos_y):
        screen_width, screen_height = self.config["screen_width"], self.config["screen_height"]
        self.offset_x = max(0, min(hero_pos_x - screen_width // 2, self.map_width - screen_width))
        self.offset_y = max(0, min(hero_pos_y - screen_height // 2, self.map_height - screen_height))
        

        # # Correct small offset errors by ensuring the offsets are multiples of tile size
        # self.offset_x = self.offset_x - (self.offset_x % self.tmx_data.tilewidth)
        # self.offset_y = self.offset_y - (self.offset_y % self.tmx_data.tileheight)

    def collided_with(self, hero):
        hero_rect = hero.get_rect()

        # Create a mask for the hero sprite
        hero_mask = hero.get_mask()
        offset = hero.get_mask_offset()

        # Check for overlap between the hero mask and the collision mask
        overlap = self.collision_mask.overlap(hero_mask, offset)

        return bool(overlap)
        
    
    def draw_mask(self, screen):
        """
         Draw the collision mask as a semi-transparent red overlay on the screen.
        """
        # Create a red surface with the same size as the collision surface and apply the mask
        red_surface = pygame.Surface((self.map_width, self.map_height), pygame.SRCALPHA)
        red_surface.fill((255, 0, 0, 100))  # Red color with transparency (alpha = 100)
    
        # Blit the collision surface onto the red surface using the mask
        red_surface.blit(self.collision_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    
        # Blit the red surface onto the screen with the map offsets
        screen.blit(red_surface, (-self.offset_x, -self.offset_y))
    
    def inspect_map(self):
        print("----- Begining of Map Inspection -----")
        print(f"Map Width (in pixels): {self.map_width}")
        print(f"Map Height (in pixels): {self.map_height}")
        print(f"Tile Width: {self.tmx_data.tilewidth}")
        print(f"Tile Height: {self.tmx_data.tileheight}")
        print(f"Number of Tiles (width x height): {self.tmx_data.width} x {self.tmx_data.height}")

        # Convert the generator to a list
        visible_layers = list(self.tmx_data.visible_layers)
        print(f"Number of Layers: {len(visible_layers)}")
    
        for layer in visible_layers:
            if isinstance(layer, pytmx.TiledObjectGroup):
                print(f"\nLayer: {layer.name}")
                print(f"Number of Objects: {len(layer)}")
                for obj in layer:
                    print(f"\nObject ID: {obj.id}")
                    print(f"Object Name: {obj.name}")
                    print(f"Object Type: {obj.type}")
                    print(f"Object Position: (x: {obj.x}, y: {obj.y})")
                    if hasattr(obj, 'width') and hasattr(obj, 'height'):
                        print(f"Object Size: (width: {obj.width}, height: {obj.height})")
                    if hasattr(obj, 'polygon'):
                        print(f"Object Polygon Points: {obj.polygon}")
                    if hasattr(obj, 'polyline'):
                        print(f"Object Polyline Points: {obj.polyline}")
                    # Check if object is correctly aligned to the grid
                    if obj.x % self.tmx_data.tilewidth != 0 or obj.y % self.tmx_data.tileheight != 0:
                        print("WARNING: Object is not aligned to the grid!")
            elif isinstance(layer, pytmx.TiledTileLayer):
                print(f"\nTile Layer: {layer.name}")
                print(f"Layer Size (in tiles): {layer.width} x {layer.height}")
    
        print("----- End of Map Inspection -----")
    
    def inspect_drawing_coordinates(self):
        screen_width, screen_height = self.config["screen_width"], self.config["screen_height"]
        start_x = max(0, self.offset_x // self.tmx_data.tilewidth)
        start_y = max(0, self.offset_y // self.tmx_data.tileheight)
        end_x = min(self.tmx_data.width, (self.offset_x + screen_width) // self.tmx_data.tilewidth + 1)
        end_y = min(self.tmx_data.height, (self.offset_y + screen_height) // self.tmx_data.tileheight + 1)
    
        print("----- Begining of Drawing Coordinate Inspection -----")
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                print(f"Tile Layer: {layer.name}")
                for x in range(start_x, end_x):
                    for y in range(start_y, end_y):
                        gid = layer.data[y][x]
                        if gid:
                            tile = self.tmx_data.get_tile_image_by_gid(gid)
                            if tile:
                                draw_pos = (x * self.tmx_data.tilewidth - self.offset_x, y * self.tmx_data.tileheight - self.offset_y)
                                print(f"Drawing tile at position: {draw_pos}")
        
            if isinstance(layer, pytmx.TiledObjectGroup):
                print(f"Object Layer: {layer.name}")
                for obj in layer:
                    draw_pos = (obj.x - self.offset_x, obj.y - self.offset_y)
                    print(f"Drawing object at position: {draw_pos}")
    
        print("----- End of Drawing Coordinate Inspection -----")

    def reset(self):
        # Reset map to its initial state
        self.offset_x = 0
        self.offset_y = 0
        # Reset any other relevant attributes

    





    











    
                

       

    
       
