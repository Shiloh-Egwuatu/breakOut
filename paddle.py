import pygame

class Paddle:
    def __init__(self, screen_width, screen_height, paddle_width=100, paddle_height=10, paddle_speed=8):
        # Set initial paddle dimensions
        self.width = paddle_width
        self.height = paddle_height
        self.speed = paddle_speed

        # Set initial paddle position (centered at bottom of screen)
        self.rect = pygame.Rect(screen_width // 2 - self.width // 2, screen_height - 50, self.width, self.height)
    
    def move(self, direction):
        """Move the paddle left or right depending on the direction input."""
        if direction == "left" and self.rect.left > 0:
            self.rect.x -= self.speed
        if direction == "right" and self.rect.right < pygame.display.get_surface().get_width():
            self.rect.x += self.speed
    
    def draw(self, screen):
        """Draw the paddle on the screen."""
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
