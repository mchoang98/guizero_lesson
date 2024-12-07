import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 35)

# Ball properties
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = 5, 5

# Paddle properties
paddle1_y, paddle2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2, HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle_speed = 7

# Scores
score1, score2 = 0, 0

# Draw everything
def draw_objects():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (10, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - 20, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)
    score_text = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 50, 10))

# Main game loop
def game_loop():
    global ball_x, ball_y, ball_dx, ball_dy, paddle1_y, paddle2_y, score1, score2

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle1_y > 0:
            paddle1_y -= paddle_speed
        if keys[pygame.K_s] and paddle1_y < HEIGHT - PADDLE_HEIGHT:
            paddle1_y += paddle_speed
        if keys[pygame.K_UP] and paddle2_y > 0:
            paddle2_y -= paddle_speed
        if keys[pygame.K_DOWN] and paddle2_y < HEIGHT - PADDLE_HEIGHT:
            paddle2_y += paddle_speed

        # Ball movement
        ball_x += ball_dx
        ball_y += ball_dy

        # Ball collision with top and bottom walls
        if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= HEIGHT:
            ball_dy = -ball_dy

        # Ball collision with paddles
        if (
            ball_x - BALL_RADIUS <= 20
            and paddle1_y < ball_y < paddle1_y + PADDLE_HEIGHT
        ) or (
            ball_x + BALL_RADIUS >= WIDTH - 20
            and paddle2_y < ball_y < paddle2_y + PADDLE_HEIGHT
        ):
            ball_dx = -ball_dx

        # Scoring
        if ball_x < 0:
            score2 += 1
            ball_x, ball_y = WIDTH // 2, HEIGHT // 2
            ball_dx = -ball_dx
        if ball_x > WIDTH:
            score1 += 1
            ball_x, ball_y = WIDTH // 2, HEIGHT // 2
            ball_dx = -ball_dx

        # Draw objects and update display
        draw_objects()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Start the game
game_loop()
