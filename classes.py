from settings import TILE, screen
import pygame

class Cell:    
    def __init__(self, x, y, w=60, h=60) -> None:
        self.wall = False
        self.limit = False
        self.cheese = False
        self.start = False
        self.x = x * TILE
        self.y = y * TILE
        self.w = w
        self.h = h
        self.rect = None

    def draw(self):
        
        if self.wall:
            self.rect = pygame.draw.rect(screen, (0, 128, 0), (self.x, self.y, self.w, self.h))
        elif self.limit:
            self.rect = pygame.draw.rect(screen, (238, 210, 0), (self.x, self.y, self.w, self.h))
        else:
            self.rect = pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.w, self.h))


        pygame.draw.line(screen, pygame.Color('black'), (self.x, self.y), (self.x + TILE, self.y), 2)
    
        pygame.draw.line(screen, pygame.Color('black'), (self.x+TILE, self.y), (self.x + TILE, self.y + TILE), 2)

        pygame.draw.line(screen, pygame.Color('black'), (self.x+TILE, self.y + TILE), (self.x, self.y + TILE), 2)

        pygame.draw.line(screen, pygame.Color('black'), (self.x, self.y + TILE), (self.x, self.y), 2)
        

    def __str__(self) -> str:
        return f"{self.wall}, {self.limit}, {self.x}, {self.y}"
    

class Rat:
    
    def __init__(self, x, y, w=50, h=50) -> None:
        self.image = pygame.image.load('sprites/sanic.png')
        self.rect = self.image.get_rect()
        self.square = None
        self.x = x + 5
        self.y = y + 5
        self.w = w
        self.h = h


    def draw(self):
        self.square = pygame.draw.rect(screen, (255, 255, 255, 1), (self.x, self.y, 0, 0))
        screen.blit(self.image, self.square)
        
class Cheese:
    
    def __init__(self, x, y, w=50, h=50) -> None:
        self.image = pygame.image.load('sprites/cheese.png')
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.w = w
        self.h = h


    def draw(self):
        rect = pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.w, self.h))
        screen.blit(self.image, rect)