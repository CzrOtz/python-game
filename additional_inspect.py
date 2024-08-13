import math

def analyze_weapon_movement(weapon, hero):
    # Calculate distances between the weapon and the pointer
    distance_to_pointer = math.sqrt((weapon.pointer_x - weapon.pos_x) ** 2 + (weapon.pointer_y - weapon.pos_y) ** 2)

    # Calculate direction vector magnitude
    direction_magnitude = math.sqrt(weapon.dir_x ** 2 + weapon.dir_y ** 2)

    # Calculate the expected direction vector using the calculated angle
    expected_dir_x = math.cos(weapon.angle)
    expected_dir_y = math.sin(weapon.angle)

    # Calculate angle in degrees
    angle_degrees = math.degrees(weapon.angle)

    # Calculate the distance between hero and weapon
    distance_to_hero = math.sqrt((hero.pos_x - weapon.pos_x) ** 2 + (hero.pos_y - weapon.pos_y) ** 2)

    # Calculate the expected scale factor for the weapon
    scale_factor = weapon.scale / hero.scale

    # Print the analysis results
    print("----- WEAPON MOVEMENT ANALYSIS -----")
    print(f"Distance to Pointer: {distance_to_pointer:.2f}")
    print(f"Direction Vector Magnitude: {direction_magnitude:.2f} (Expected: 1.0)")
    print(f"Calculated Angle (degrees): {angle_degrees:.2f}")
    print(f"Expected Direction Vector: (x: {expected_dir_x:.2f}, y: {expected_dir_y:.2f})")
    print(f"Actual Direction Vector: (x: {weapon.dir_x:.2f}, y: {weapon.dir_y:.2f})")
    print(f"Distance from Hero to Weapon: {distance_to_hero:.2f}")
    print(f"Scale Factor (Weapon/Hero): {scale_factor:.2f}")
    print(f"Weapon Position: ({weapon.pos_x}, {weapon.pos_y})")
    print(f"Hero Position: ({hero.pos_x}, {hero.pos_y})")
    print(f"Pointer Position: ({weapon.pointer_x}, {weapon.pointer_y})")
    print("-------------------------------\n")


def view_masks(map, hero, weapon, ghost, screen):
    map.draw_mask(screen)
    weapon.draw_mask(screen, map.offset_x, map.offset_y)
    hero.draw_mask(screen, map.offset_x, map.offset_y)
    ghost.draw_all_masks(map)

