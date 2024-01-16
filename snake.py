import pygame
import time
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 15
BLOCK_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize clock
clock = pygame.time.Clock()

# Initialize font
font = pygame.font.SysFont(None, 40)

# Initialize snake direction
snake_direction = "RIGHT"

# Initialize snake
snake = [[WIDTH / 2, HEIGHT / 2]]

# Function to draw the snake
def draw_snake(snake, block_size):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], block_size, block_size])

# Function to display score
def display_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [10, 10])

# Main game loop
def game_loop():
    global snake, snake_direction
    game_over = False
    game_close = False

    # Initialize food
    food = [random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE),
            random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)]

    # Initial score
    score = 0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            score_text = font.render("Your Score is: " + str(score), True, WHITE)
            screen.blit(score_text, [WIDTH / 4, HEIGHT / 2])
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not snake_direction == "RIGHT":
                    snake_direction = "LEFT"
                elif event.key == pygame.K_RIGHT and not snake_direction == "LEFT":
                    snake_direction = "RIGHT"
                elif event.key == pygame.K_UP and not snake_direction == "DOWN":
                    snake_direction = "UP"
                elif event.key == pygame.K_DOWN and not snake_direction == "UP":
                    snake_direction = "DOWN"

        # Move the snake
        if snake_direction == "LEFT":
            snake[0][0] -= BLOCK_SIZE
        elif snake_direction == "RIGHT":
            snake[0][0] += BLOCK_SIZE
        elif snake_direction == "UP":
            snake[0][1] -= BLOCK_SIZE
        elif snake_direction == "DOWN":
            snake[0][1] += BLOCK_SIZE

        # Check for collisions with the walls
        if (
            snake[0][0] < 0
            or snake[0][0] >= WIDTH
            or snake[0][1] < 0
            or snake[0][1] >= HEIGHT
        ):
            game_close = True

        # Check for collisions with itself
        for segment in snake[1:]:
            if snake[0] == segment:
                game_close = True

        # Check for collision with food
        if snake[0][0] == food[0] and snake[0][1] == food[1]:
            food = [
                random.randrange(0, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                random.randrange(0, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE,
            ]
            score += 1
        else:
            # Remove the last segment of the snake
            snake.pop()

        # Draw everything
        screen.fill(BLACK)
        draw_snake(snake, BLOCK_SIZE)
        pygame.draw.rect(screen, RED, [food[0], food[1], BLOCK_SIZE, BLOCK_SIZE])
        display_score(score)
        pygame.display.flip()

        # Set the frames per second
        clock.tick(FPS)

    pygame.quit()
    quit()

# Run the game loop
game_loop()
