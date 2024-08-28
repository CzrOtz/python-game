import pygame

def game_over(screen):
    font = pygame.font.Font(None, 74)
    button_font = pygame.font.Font(None, 50)
    
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    exit_button = button_font.render("Exit", True, (255, 255, 255))
    menu_button = button_font.render("Go Back to Menu", True, (255, 255, 255))
    
    screen_width, screen_height = screen.get_size()
    
    exit_button_rect = exit_button.get_rect(center=(screen_width // 3, 2 * screen_height // 3))
    menu_button_rect = menu_button.get_rect(center=(2 * screen_width // 3, 2 * screen_height // 3))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0  # Exit the game
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if exit_button_rect.collidepoint(mouse_pos):
                    return 0  # Exit the game
                elif menu_button_rect.collidepoint(mouse_pos):
                    return 1  # Go back to main menu

        screen.fill((0, 0, 0))  # Black background
        
        # Display "Game Over" text
        text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 3))
        screen.blit(game_over_text, text_rect)
        
        # Create and display "Exit" button
        pygame.draw.rect(screen, (100, 100, 100), exit_button_rect)
        screen.blit(exit_button, exit_button_rect)
        
        # Create and display "Go Back to Menu" button
        pygame.draw.rect(screen, (100, 100, 100), menu_button_rect)
        screen.blit(menu_button, menu_button_rect)
        
        pygame.display.flip()

    return 0  # Default to exiting the game if the loop is somehow broken
