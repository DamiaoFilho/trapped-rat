from settings import TILE, screen
import pygame

class Cell:
    
    def __init__(self, x, y, w=50, h=50) -> None:
        self.wall = False
        self.limit = False
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        x, y = self.x * TILE, self.y * TILE
        
        if self.wall:
            pygame.draw.rect(screen, (0, 128, 0), (x, y, self.w, self.h))
        elif self.limit:
            pygame.draw.rect(screen, (238, 210, 0), (x, y, self.w, self.h))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (x, y, self.w, self.h))


        pygame.draw.line(screen, pygame.Color('black'), (x, y), (x + TILE, y), 2)
    
        pygame.draw.line(screen, pygame.Color('black'), (x+TILE, y), (x + TILE, y + TILE), 2)

        pygame.draw.line(screen, pygame.Color('black'), (x+TILE, y + TILE), (x, y + TILE), 2)

        pygame.draw.line(screen, pygame.Color('black'), (x, y + TILE), (x, y), 2)
        

    def __str__(self) -> str:
        return f"{self.wall}, {self.limit}, {self.x}, {self.y}"