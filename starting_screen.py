import pygame

class StartScreen:
    def __init__(self, ai_settings, screen):
        """Initialize the starting screen image and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the starting screen image and get its rect
        self.image = pygame.image.load('images/startScreen.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery


    def blitme(self):
        """Draw the starting screen at its current location"""
        self.screen.blit(self.image, self.rect)

