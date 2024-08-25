import pygame
import sys
from configurations import config

def game_over(screen):
    running = True
    while running:
        screen.fill((0, 0, 0))  # Clear the screen with a black background
        
        # Render the game over text
        font = pygame.font.Font(None, 74)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        menu_text = font.render("Press Enter for Main Menu", True, (255, 255, 255))
        
        screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, screen.get_height() // 2 - 100))
        screen.blit(menu_text, (screen.get_width() // 2 - menu_text.get_width() // 2, screen.get_height() // 2 + 100))
        
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Press Enter to return to the main menu
                    return 1  # Transition to the MAIN_MENU state

        pygame.display.flip()
        config.clock.tick(config.FPS)
