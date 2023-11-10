import pygame
from settings import TILE, screen

class Cell:    
    def __init__(self, i, j, x, y, w=60, h=60) -> None:
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
        self.i = i
        self.j = j

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
    
    def __init__(self, i, j, x, y, w=50, h=50) -> None:
        self.image = pygame.image.load('sprites/sanic.png')
        self.rect = self.image.get_rect()
        self.square = None
        self.x = x 
        self.y = y 
        self.w = w
        self.h = h
        self.i = i
        self.j = j

        self.trajetory = []


    def draw(self):
        self.square = pygame.draw.rect(screen, (255, 255, 255, 1), (self.x, self.y, 0, 0))
        screen.blit(self.image, self.square.center)

    def move(self, grid_cells):
        flag = False        

        #Check R
        if self.checkCell(grid_cells[self.i][self.j+1]):
            cellToChange = grid_cells[self.i][self.j+1]
            flag = True
        
        #Check L
        elif self.checkCell(grid_cells[self.i][self.j-1]): 
            cellToChange = grid_cells[self.i][self.j-1]
            flag = True
            
        #Check D
        elif self.checkCell(grid_cells[self.i+1][self.j]):
            cellToChange = grid_cells[self.i+1][self.j]
            flag = True
        
        #Check U
        elif self.checkCell(grid_cells[self.i-1][self.j]): 
            cellToChange = grid_cells[self.i-1][self.j]
            flag = True

        if flag:
            self.trajetory.append(cellToChange)
            print(len(self.trajetory))
            self.x = cellToChange.x
            self.y = cellToChange.y
            self.i = cellToChange.i
            self.j = cellToChange.j
            cellToChange.visited = True
            return flag
        else:
            return flag



    def checkCell(self, nextCell):
        if nextCell.wall == False and nextCell.limit == False and nextCell.visited == False:
            return True
        return False
        
    def goBack(self):
        print(len(self.trajetory))
        previousCell = self.trajetory.pop()
        self.x -= (previousCell.x - self.trajetory[-1].x)
        self.y -= (previousCell.y - self.trajetory[-1].y)
        self.i = self.trajetory[-1].i
        self.j = self.trajetory[-1].j
        
class Cheese:
    
    def __init__(self, i, j, x, y, w=50, h=50) -> None:
        self.image = pygame.image.load('sprites/cheese.png')
        self.rect = self.image.get_rect()
        self.x = x + 5 
        self.y = y + 5 
        self.w = w
        self.h = h
        self.i = i
        self.j = j


    def draw(self):
        rect = pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 0, 0))
        screen.blit(self.image, rect)