import pygame

class Brick:
    def __init__(self, x, y, width, height, color):
        """Initialize each brick with its position, size, and color."""
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.is_active = True

    def draw(self, screen):
        """Draw the brick on the screen if it is active."""
        if self.is_active:
            pygame.draw.rect(screen, self.color, self.rect)


class BrickWall:
    def __init__(self, screen_width, rows=5, cols=10, brick_width=80, brick_height=30, padding=5):
        """Create a grid of bricks."""
        self.bricks = []
        self.rows = rows
        self.cols = cols
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.padding = padding
        self.create_wall(screen_width)

    def create_wall(self, screen_width):
        """Initialize the wall of bricks by placing them in rows and columns."""
        offset_x = (screen_width - (self.cols * (self.brick_width + self.padding))) // 2
        for row in range(self.rows):
            for col in range(self.cols):
                x = offset_x + col * (self.brick_width + self.padding)
                y = row * (self.brick_height + self.padding) + 50
                color = (255, 0, 0) if row % 2 == 0 else (0, 0, 255)
                brick = Brick(x, y, self.brick_width, self.brick_height, color)
                self.bricks.append(brick)

    def draw(self, screen):
        """Draw all active bricks."""
        for brick in self.bricks:
            brick.draw(screen)
