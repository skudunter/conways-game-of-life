from cell import Cell


class CellManager:
    def __init__(self, gridSize, screenWidth, screenHeight, cellColor):
        self.gridSize = gridSize
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.cellColor = cellColor
        self.cells = [[0 for i in range(screenWidth//gridSize)]
                      for j in range(screenHeight//gridSize)]

    def spawn_cell(self, x, y):
        gridX, gridY = x // self.gridSize, y // self.gridSize
        self.cells[gridY][gridX] = Cell(
            gridX * self.gridSize, gridY * self.gridSize, self.gridSize, self.cellColor)

    def erase_cell(self, x, y):
        gridX, gridY = x // self.gridSize, y // self.gridSize
        self.cells[gridY][gridX] = 0

    def display_cells(self, screen):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                if self.cells[i][j] != 0:
                    self.cells[i][j].display(screen)

    def check_neighbors(self, x, y):
        neighbors = 0
        for i in range(max(0, x - 1), min(x + 2, len(self.cells))):
            for j in range(max(0, y - 1), min(y + 2, len(self.cells[0]))):
                if (i != x or j != y) and self.cells[i][j] != 0:
                    neighbors += 1
        return neighbors

    def update(self):
        new_cells = [[0 for i in range(self.screenWidth//self.gridSize)]
                     for j in range(self.screenHeight//self.gridSize)]
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                neighbors = self.check_neighbors(i, j)
                if self.cells[i][j] != 0:
                    if neighbors < 2 or neighbors > 3:
                        new_cells[i][j] = 0
                    else:
                        new_cells[i][j] = self.cells[i][j]
                else:
                    if neighbors == 3:
                        new_cells[i][j] = Cell(
                            j * self.gridSize, i * self.gridSize, self.gridSize, self.cellColor)
        self.cells = new_cells

    def restart(self,):
        self.cells = [[0 for i in range(self.screenWidth//self.gridSize)]
                      for j in range(self.screenHeight//self.gridSize)]
