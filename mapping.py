from classes import Cell

mapping = []
grid_cells = []

with open("mapping.txt") as txt:
    dimensions = txt.readline().split(" ")
    cols, rows = int(dimensions[0])+1, int(dimensions[1])+1

    for line in txt.readlines():
        line = line.strip()
        aux = line.split(" ")
        for value in aux:
            mapping.append(value)

    aux = 0
    print(len(mapping))
    print(cols, rows)
    for row in range(rows):
        for col in range(cols):
            if(row==0 or row == rows-1):
                cell = Cell(col, row)
                cell.limit = True
                grid_cells.append(cell)
            elif(col == 0 or col == cols-1):
                cell = Cell(col, row)
                cell.limit = True
                grid_cells.append(cell)
            else:
                cell = Cell(col, row)
                if int(mapping[aux]) == 1:
                    cell.wall = True
                else:
                    cell.wall = False
                grid_cells.append(cell)
                print(aux)
                aux += 1
