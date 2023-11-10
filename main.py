import pygame
from settings import RES, screen
from mapping import grid_cells, start_cell, end_cell, grid_walls
from classes import Rat, Cheese
#PYGAME SETUP
pygame.init()
clock = pygame.time.Clock()
running = True
dt = 0


#MUSIC
pygame.mixer.init()
pygame.mixer.music.load("music/sanicTheme.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()



stack = []
rat = Rat(start_cell.i, start_cell.j, start_cell.x, start_cell.y)
rat.trajetory.append(start_cell)

cheese = Cheese(end_cell.i, end_cell.j, end_cell.x, end_cell.y)

while running:
    #FINISH
    if rat.i == cheese.i and rat.j == cheese.j:
        running = False
        
    #PYGAME EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")

    #MAIN

    #DRAW THINGS
    for line in grid_cells:
        for cell in line:
            cell.draw()
    rat.draw()
    cheese.draw()

    #MOVE
    if rat.move(grid_cells) is False:
        rat.goBack()

    #PYGAME STUFF
    pygame.display.flip()
    dt = clock.tick(2)

pygame.mixer.music.load("music/victoryFanfare.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
pygame.time.delay(5000)
pygame.quit()
