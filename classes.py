import pygame
from settings import TILE, screen

class Cell:    
    def __init__(self, x, y, w=60, h=60) -> None:
        self.visited = False
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
        elif self.visited:
            self.rect = pygame.draw.rect(screen, (150, 75, 0), (self.x, self.y, self.w, self.h))
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
        self.x = x 
        self.y = y 
        self.w = w
        self.h = h
        self.trajetory = []


    def draw(self):
        self.square = pygame.draw.rect(screen, (255, 255, 255, 1), (self.x, self.y, 0, 0))
        screen.blit(self.image, self.square)

    def move(self, grid_cells):
        cellToChange = self
        for i, l in enumerate(grid_cells):
            for j, cell in enumerate(l):
                if cell.x == self.x and cell.y == self.y:

                    #Check R
                    if j+1 < len(l) and self.checkCell(grid_cells[i][j+1]):
                        print("R") 
                        cellToChange = grid_cells[i][j+1]
                    
                    #Check L
                    elif j-1 >= 0 and self.checkCell(grid_cells[i][j+1]): 
                        print("L") 
                        cellToChange = grid_cells[i][j-1]
                        
                    #Check D
                    elif i+1 < len(grid_cells) and self.checkCell(grid_cells[i+1][j]):
                        print("D") 
                        cellToChange = grid_cells[i+1][j]
                    
                    #Check U
                    elif i-1 >= 0 and self.checkCell(grid_cells[i-1][j]): 
                        print("U") 
                        cellToChange = grid_cells[i-1][j]

                

        self.x = cellToChange.x
        self.y = cellToChange.y
        cellToChange.visited = True
        current_cell = cellToChange
        #check L



    def checkCell(self, nextCell):
        if nextCell.wall == False and nextCell.limit == False and nextCell.visited == False:
            return True
        return False
        
        
class Cheese:
    
    def __init__(self, x, y, w=50, h=50) -> None:
        self.image = pygame.image.load('sprites/cheese.png')
        self.rect = self.image.get_rect()
        self.x = x + 5 
        self.y = y + 5 
        self.w = w
        self.h = h


    def draw(self):
        rect = pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 0, 0))
        screen.blit(self.image, rect)