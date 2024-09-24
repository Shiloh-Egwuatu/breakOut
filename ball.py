import pygame

class Ball:
    def __init__(self, screen_width, screen_height, ball_size=20, ball_speed_x=5, ball_speed_y=-5):
        # Set initial ball size and speed
        self.size = ball_size
        self.speed_x = ball_speed_x
        self.speed_y = ball_speed_y

        # Initialize ball position in the center of the screen
        self.rect = pygame.Rect(screen_width // 2 - self.size // 2, screen_height // 2 - self.size // 2, self.size, self.size)
    
    def move(self):
        """Move the ball in both x and y directions."""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def bounce(self, axis):
        """Bounce the ball by reversing its direction along the specified axis."""
        if axis == "x":
            self.speed_x *= -1
        if axis == "y":
            self.speed_y *= -1

    def reset(self, screen_width, screen_height):
        """Reset the ball to the center of the screen."""
        self.rect.x = screen_width // 2 - self.size // 2
        self.rect.y = screen_height // 2 - self.size // 2
        self.speed_y *= -1  # Reverse the Y direction after resetting

    def draw(self, screen):
        """Draw the ball on the screen."""
        pygame.draw.ellipse(screen, (255, 255, 255), self.rect)
