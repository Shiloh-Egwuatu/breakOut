import pygame
from paddle import Paddle
from ball import Ball
from bricks import BrickWall

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BG_COLOR = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")
clock = pygame.time.Clock()

# Initialize game objects
paddle = Paddle(WIDTH, HEIGHT)
ball = Ball(WIDTH, HEIGHT)
brick_wall = BrickWall(WIDTH)

# Function to handle collision detection
def check_collisions():
    # Ball and paddle collision
    if ball.rect.colliderect(paddle.rect):
        ball.bounce("y")
    
    # Ball and bricks collision
    for brick in brick_wall.bricks:
        if brick.is_active and ball.rect.colliderect(brick.rect):
            ball.bounce("y")
            brick.is_active = False  # Remove the brick after collision

    # Ball hitting left or right walls
    if ball.rect.left <= 0 or ball.rect.right >= WIDTH:
        ball.bounce("x")

    # Ball hitting the top wall
    if ball.rect.top <= 0:
        ball.bounce("y")

    # Ball falling below the screen
    if ball.rect.bottom >= HEIGHT:
        ball.reset(WIDTH, HEIGHT)  # Reset ball if it falls

# Main Game function
def main():
    # Main game loop
    run = True
    while run:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Paddle movement (with key press detection)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move("left")
        if keys[pygame.K_RIGHT]:
            paddle.move("right")
        
        # Update game objects
        ball.move()
        check_collisions()

        # Drawing everything
        screen.fill(BG_COLOR)
        paddle.draw(screen)
        ball.draw(screen)
        brick_wall.draw(screen)

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(FPS)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
