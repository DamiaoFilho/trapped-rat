from settings import TILE, screen
import pygame

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False

    def draw_current_cell(self):
        x, y = self.x * TILE, self.y * TILE
        pygame.draw.rect(screen, pygame.Color('yellow'), (x + 2, y + 2, TILE - 2, TILE - 2))

    def draw(self):
        x, y = self.x * TILE, self.y * TILE

        if self.visited:
            pygame.draw.rect(screen, pygame.Color('black'), (x, y, TILE, TILE))

        if self.walls['top']:
            pygame.draw.line(screen, pygame.Color('darkorange'), (x, y), (x + TILE, y), 2)
        
        if self.walls['right']:
            pygame.draw.line(screen, pygame.Color('darkorange'), (x+TILE, y), (x + TILE, y + TILE), 2)

        if self.walls['bottom']:
            pygame.draw.line(screen, pygame.Color('darkorange'), (x+TILE, y + TILE), (x, y + TILE), 2)

        if self.walls['left']:
            pygame.draw.line(screen, pygame.Color('darkorange'), (x, y + TILE), (x, y), 2)
