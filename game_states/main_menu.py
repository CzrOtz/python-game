import pygame
import sys
from configurations import config

def main_menu(screen):
    running = True
    while running:
        screen.fill((0, 0, 0))  # Clear the screen with a black background
        
        # Render the main menu options
        font = pygame.font.Font(None, 74)
        play_text = font.render("Play Game", True, (255, 255, 255))
        config.screen.blit(play_text, (screen.get_width() // 2 - play_text.get_width() // 2, screen.get_height() // 2 - 100))
        
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Press Enter to start the game
                    return 2  # Transition to the PLAYING state

        pygame.display.flip()
        config.clock.tick(config.FPS)