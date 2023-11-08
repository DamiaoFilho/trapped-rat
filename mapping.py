from classes import Cell

mapping = []
grid_cells = []

with open("mapping.txt") as txt:
    dimensions = txt.readline().split(" ")
    cols, rows = int(dimensions[0])+2, int(dimensions[1])+2

    for line in txt.readlines():
        line = line.strip()
        aux = line.split(" ")
        for value in aux:
            mapping.append(value)

    grid_walls = []
    aux = 0
    for row in range(rows):
        for col in range(cols):
            cell = Cell(col, row)

            if(row == 1 and col == 1):
                start_cell = cell

            if(row==0 or row == rows-1):
                cell.limit = True
            elif(col == 0 or col == cols-1):
                cell.limit = True
            else:
                if int(mapping[aux]) == 1:
                    cell.wall = True
                    grid_walls.append(cell)
                else:
                    cell.wall = False
                aux += 1
            
            grid_cells.append(cell)
