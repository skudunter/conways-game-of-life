import pygame
import keyboard
import time
from cellManager import CellManager

# pygame setup
pygame.init()

# global vars
gridSize = 20
screenWidth = (pygame.display.Info().current_w // gridSize) * gridSize
screenHeight = ((pygame.display.Info().current_h - 60) // gridSize) * gridSize
backgroundColor = pygame.Color('#0F100F')
gridColor = pygame.Color('#E3D3E4')
cellColor = pygame.Color('#00FFD1')
running = True
hasGameStarted = False
showGrid = False
drawing = False

# screen setup
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
font = pygame.font.Font('font.ttf', 20)
pygame.display.set_caption("Conways game of life")

cellManager = CellManager(gridSize, screenWidth, screenHeight, cellColor)


def doGridFunctionality(gridSize, screenWidth, screenHeight, gridColor, screen, showGrid):
    if keyboard.is_pressed('g'):
        showGrid = not showGrid
    if showGrid:
        for x in range(0, screenWidth, gridSize):
            pygame.draw.line(screen, gridColor, (x, 0), (x, screenHeight))
        for y in range(0, screenHeight, gridSize):
            pygame.draw.line(screen, gridColor, (0, y), (screenWidth, y))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if hasGameStarted == False:
                    cellManager.spawn_cell(event.pos[0], event.pos[1])
                drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                # Get the x, y position of the mouse click
                x, y = pygame.mouse.get_pos()
                # Spawn a new cell at the grid coordinates
                if (hasGameStarted == False):
                    cellManager.spawn_cell(x, y)
    dt = clock.tick(60) / 1000
    screen.fill(backgroundColor)
    # RENDER YOUR GAME HERE
    doGridFunctionality(gridSize, screenWidth, screenHeight,
                        gridColor, screen, showGrid)
    # write text to the top left corner
    cellManager.display_cells(screen)
    if keyboard.is_pressed('space'):
        hasGameStarted = True
    if keyboard.is_pressed('r'):
        hasGameStarted = False
        cellManager.restart()
    if (hasGameStarted):
        cellManager.update()
        time.sleep(0.5)

    text = font.render("Game has started: " +
                       str(hasGameStarted), True, (255, 255, 255))
    screen.blit(text, (10, 10))
    text = font.render("Grid is active: " + str(showGrid),
                       True, (255, 255, 255))
    screen.blit(text, (10, 40))
    text = font.render(
        "Framerate: " + str(round(clock.get_fps())), True, (255, 255, 255))
    screen.blit(text, (10, 70))
    pygame.display.flip()
