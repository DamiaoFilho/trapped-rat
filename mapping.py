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

    aux = 0
    print(len(mapping))
    print(mapping)
    print(cols, rows)
    for row in range(rows):
        for col in range(cols):
            cell = Cell(col, row)
            if(row==0 or row == rows-1):
                cell.limit = True
            elif(col == 0 or col == cols-1):
                cell.limit = True
            else:
                print(row, col, mapping[aux])
                if int(mapping[aux]) == 1:
                    cell.wall = True
                else:
                    cell.wall = False
                print(cell)
                aux += 1
            grid_cells.append(cell)
