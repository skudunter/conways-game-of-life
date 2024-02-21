import pygame
import keyboard
import time
from cellManager import CellManager

# Initialize pygame
pygame.init()

# Define constants
GRID_SIZE = 20
SCREEN_WIDTH = (pygame.display.Info().current_w // GRID_SIZE) * GRID_SIZE
SCREEN_HEIGHT = ((pygame.display.Info().current_h - 60) //
                 GRID_SIZE) * GRID_SIZE
BACKGROUND_COLOR = pygame.Color('#0F100F')
GRID_COLOR = pygame.Color('#E3D3E4')
CELL_COLOR = pygame.Color('#00FFD1')

# Initialize variables
running = True
has_game_started = False
show_grid = False
drawing = False

# Set up screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Conways game of life")

# Set up clock and font
clock = pygame.time.Clock()
font = pygame.font.Font('font.ttf', 20)

# Initialize cell manager
cell_manager = CellManager(GRID_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, CELL_COLOR)

# Define a custom event
UPDATE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(UPDATE_EVENT, 500)


def draw_grid(grid_size, screen_width, screen_height, grid_color, screen, show_grid):
    """Draws a grid on the screen if show_grid is True."""
    if keyboard.is_pressed('g'):
        show_grid = not show_grid
    if show_grid:
        for x in range(0, screen_width, grid_size):
            pygame.draw.line(screen, grid_color, (x, 0), (x, screen_height))
        for y in range(0, screen_height, grid_size):
            pygame.draw.line(screen, grid_color, (0, y), (screen_width, y))


while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not has_game_started:
            cell_manager.spawn_cell(event.pos[0], event.pos[1])
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing and not has_game_started:
            x, y = pygame.mouse.get_pos()
            cell_manager.spawn_cell(x, y)
        elif event.type == UPDATE_EVENT and has_game_started:
            cell_manager.update()

    # Update screen
    dt = clock.tick(60) / 1000
    screen.fill(BACKGROUND_COLOR)
    draw_grid(GRID_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT,
              GRID_COLOR, screen, show_grid)
    cell_manager.display_cells(screen)

    # Game controls
    if keyboard.is_pressed('space'):
        has_game_started = True
    if keyboard.is_pressed('r'):
        has_game_started = False
        cell_manager.restart()

    # Display game status
    screen.blit(font.render(f"Game has started: {
                has_game_started}", True, (255, 255, 255)), (10, 10))
    screen.blit(font.render(f"Grid is active: {
                show_grid}", True, (255, 255, 255)), (10, 40))
    screen.blit(font.render(
        f"Framerate: {round(clock.get_fps())}", True, (255, 255, 255)), (10, 70))

    pygame.display.flip()
