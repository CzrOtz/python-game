import pygame
from configurations.main_menu_config import main_menu_config

def main_menu(screen):
    font_header = pygame.font.Font(None, main_menu_config["header_font_size"])
    font_button = pygame.font.Font(None, main_menu_config["button_font_size"])
    
    header_text = font_header.render(main_menu_config["header_text"], True, main_menu_config["header_text_color"])
    button_text = font_button.render(main_menu_config["button_text"], True, main_menu_config["button_text_color"])
    
    screen_width, screen_height = screen.get_size()
    
    header_rect = header_text.get_rect(center=(screen_width // 2, main_menu_config["header_y_position"]))
    button_rect = pygame.Rect(
        (screen_width // 2 - main_menu_config["button_width"] // 2, main_menu_config["button_y_position"]),
        (main_menu_config["button_width"], main_menu_config["button_height"])
    )
    button_text_rect = button_text.get_rect(center=button_rect.center)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0  # Exit the game
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(f"Mouse button down at {mouse_pos}")  # Debugging line
                if button_rect.collidepoint(mouse_pos):
                    print("Button clicked!")  # Debugging line
                    return 2  # Start the game

        screen.fill(main_menu_config["background_color"])
        
        # Draw header text
        screen.blit(header_text, header_rect)
        
        # Draw button
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, main_menu_config["button_hover_color"], button_rect, border_radius=main_menu_config["button_border_radius"])
        else:
            pygame.draw.rect(screen, main_menu_config["button_color"], button_rect, border_radius=main_menu_config["button_border_radius"])
        screen.blit(button_text, button_text_rect)
        
        pygame.display.flip()