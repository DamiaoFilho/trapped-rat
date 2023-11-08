import pygame
from settings import RES, screen
from mapping import grid_cells, start_cell, grid_walls
from classes import Rat
#PYGAME SETUP
pygame.init()
clock = pygame.time.Clock()
running = True
dt = 0


stack = []
ratPos = pygame.Vector2(start_cell.x, start_cell.y)

while running:
    #PYGAME EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")

    #MAIN
    for cell in grid_cells:
        cell.draw()

    rat = Rat(ratPos.x, ratPos.y)
    rat.draw()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        ratPos.y -=  5
    if keys[pygame.K_s]:
        ratPos.y += 5
    if keys[pygame.K_a]:
        ratPos.x -= 5
    if keys[pygame.K_d]:
        ratPos.x += 5

    #PYGAME STUFF
    pygame.display.flip()
    dt = clock.tick(10) / 1000

pygame.quit()
