#pygamesetup
import pygame
from random import choice
TILE = 50
RES = WIDTH, HEIGHT = 601, 451

pygame.init()
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
running = True
dt = 0
####################################################
#CLASSES

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

##############################################
#MAPPING 

txt = open("mapping.txt", "r")
dimensions = txt.readline().split(" ")
cols, rows = int(dimensions[0]), int(dimensions[1])

mapping = []
for line in txt.readlines():
    aux = line.split(" ")
    for value in aux:
        mapping.append(value)
print(mapping)

aux = 0
grid_cells = []
for row in range(rows):
    for col in range(cols):
        cell = Cell(col, row)
        if int(mapping[aux]) == 1:
            cell.walls.values = True
        else:
            cell.walls.values = False

current_cell = grid_cells[0]

stack = []        
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    [cell.draw() for cell in grid_cells]
    current_cell.draw_current_cell()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
