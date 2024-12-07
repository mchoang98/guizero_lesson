import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions and grid
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 600
BLOCK_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // BLOCK_SIZE, SCREEN_HEIGHT // BLOCK_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
COLORS = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # Magenta
    (128, 0, 128)  # Purple
]

# Tetrimino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]   # Z
]

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

# Grid and Tetrimino setup
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

class Tetrimino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def collides(self, dx=0, dy=0):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    nx, ny = self.x + x + dx, self.y + y + dy
                    if nx < 0 or nx >= GRID_WIDTH or ny >= GRID_HEIGHT or (ny >= 0 and grid[ny][nx]):
                        return True
        return False

    def lock(self):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell and self.y + y >= 0:
                    grid[self.y + y][self.x + x] = self.color

# Clear complete lines
def clear_lines():
    global grid
    grid = [row for row in grid if any(cell == 0 for cell in row)]
    cleared_lines = GRID_HEIGHT - len(grid)
    for _ in range(cleared_lines):
        grid.insert(0, [0] * GRID_WIDTH)

# Draw grid
def draw_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x]:
                pygame.draw.rect(screen, grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (SCREEN_WIDTH, y))

# Main game loop
def game_loop():
    current_piece = Tetrimino()
    drop_time = 500
    last_time = pygame.time.get_ticks()
    running = True

    while running:
        screen.fill(BLACK)
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not current_piece.collides(dx=-1):
                        current_piece.x -= 1
                if event.key == pygame.K_RIGHT:
                    if not current_piece.collides(dx=1):
                        current_piece.x += 1
                if event.key == pygame.K_DOWN:
                    if not current_piece.collides(dy=1):
                        current_piece.y += 1
                if event.key == pygame.K_UP:
                    current_piece.rotate()
                    if current_piece.collides():
                        for _ in range(3):  # Rotate back if collision
                            current_piece.rotate()

        # Auto drop piece
        if pygame.time.get_ticks() - last_time > drop_time:
            if not current_piece.collides(dy=1):
                current_piece.y += 1
            else:
                current_piece.lock()
                clear_lines()
                current_piece = Tetrimino()
                if current_piece.collides():
                    running = False  # Game over
            last_time = pygame.time.get_ticks()

        # Draw current piece
        for y, row in enumerate(current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, current_piece.color, 
                                     ((current_piece.x + x) * BLOCK_SIZE, 
                                      (current_piece.y + y) * BLOCK_SIZE, 
                                      BLOCK_SIZE, BLOCK_SIZE))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

# Start the game
game_loop()
