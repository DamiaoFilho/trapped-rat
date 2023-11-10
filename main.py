import pygame
from settings import RES, screen
from mapping import grid_cells, start_cell, end_cell, grid_walls
from classes import Rat, Cheese
#PYGAME SETUP
pygame.init()
clock = pygame.time.Clock()
running = True
dt = 0


stack = []
rat = Rat(start_cell.x, start_cell.y)
cheese = Cheese(end_cell.x, end_cell.y)

while running:
    #PYGAME EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")

    #MAIN
    for line in grid_cells:
        for cell in line:
            cell.draw()

    rat.draw()
    cheese.draw()


    rat.move(grid_cells)

    #PYGAME STUFF
    pygame.display.flip()
    dt = clock.tick(1)

pygame.quit()
