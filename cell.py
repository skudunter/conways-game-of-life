import pygame

class Cell:
    def __init__(self, x, y,gridSize,color):
        self.x = x
        self.y = y
        self.color = color
        self.gridSize = gridSize
    def display(self,screen):
     pygame.draw.rect(screen, self.color, (self.x, self.y, self.gridSize, self.gridSize))