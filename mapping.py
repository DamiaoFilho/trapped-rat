from classes import Cell

mapping = []
grid_cells = []

with open("mapping.txt") as txt:
    dimensions = txt.readline().split(" ")
    cols, rows = int(dimensions[0]), int(dimensions[1])

    for line in txt.readlines():
        line = line.strip()
        aux = line.split(" ")
        for value in aux:
            mapping.append(value)

    aux = 0
    grid_cells = []
    for row in range(rows):
        for col in range(cols):
            cell = Cell(col, row)
            print(cell.walls)
            if int(mapping[aux]) == 1:
                cell.walls = {x:True for x in cell.walls.keys()}
            else:
                cell.walls = {x:False for x in cell.walls.keys()}
            print(cell.walls)
            grid_cells.append(cell)
            aux += 1

    current_cell = grid_cells[0]