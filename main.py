import pygame
from settings import RES, screen
from mapping import grid_cells

#PYGAME SETUP
pygame.init()
clock = pygame.time.Clock()
running = True
dt = 0




while running:
    #PYGAME STUUF
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")

    #MAIN
    for cell in grid_cells:
        cell.draw()

    #PYGAME STUFF
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
