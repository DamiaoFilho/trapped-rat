from classes import Cell

mapping = []
grid_cells = [] 

with open("mapping.txt") as txt:
    dimensions = txt.readline().split(" ")
    cols, rows = int(dimensions[0])+2, int(dimensions[1])+2

    for line in txt.readlines():
        line = line.replace("\n", "")
        aux = line.split(" ")
        for value in aux:
            mapping.append(value)

    grid_walls = []
    aux = 0
    for row in range(rows):
        line = []
        for col in range(cols):
            cell = Cell(col, row)

            if(row==0 or row == rows-1):
                cell.limit = True
            elif(col == 0 or col == cols-1):
                cell.limit = True
            else:
                if mapping[aux] == "1":
                    cell.wall = True
                    grid_walls.append(cell)
                elif mapping[aux] == "m":
                    cell.wall = False
                    cell.visited = True
                    start_cell = cell
                elif mapping[aux] == "e":
                    cell.wall = False
                    end_cell = cell
                else:
                    cell.wall = False
                aux += 1
            line.append(cell)
        grid_cells.append(line)
            