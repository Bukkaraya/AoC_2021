def get_grid_length(lines):
    x_max = 0
    y_max = 0

    for line in lines:
        current_x = max(line[0][0], line[1][0])
        current_y =max(line[0][1], line[1][1])

        if x_max < current_x:
            x_max = current_x
        if y_max < current_y:
            y_max = current_y


    return max(x_max, y_max)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().split("\n")

    lines = [[
        list(map(int, i.split(","))) for i in l.replace("->", "").split()
    ] for l in lines]

    grid_length = get_grid_length(lines)
    grid = [[0 for _ in range(grid_length + 1)] for _ in range(grid_length + 1)]

    for line in lines:
        x1 = line[0][0]
        x2 = line[1][0]
        
        y1 = line[0][1]
        y2 = line[1][1]
        
        if x1 == x2:
            x = x1
            y_base = min(y1, y2)
            delta = abs(y2 - y1)

            for i in range(delta + 1):
                grid[y_base + i][x] += 1

        if y1 == y2:
            y = y1
            x_base = min(x1, x2)
            delta = abs(x2 - x1)

            for i in range(delta + 1):
                grid[y][x_base + i] += 1

    num_overlaps = 0
    for line in grid:
        for l in line:
            if l >= 2:
                num_overlaps += 1 
    print(f"Result for Part 1: {num_overlaps}")

    for line in lines:
        x1 = line[0][0]
        x2 = line[1][0]
        
        y1 = line[0][1]
        y2 = line[1][1]

        if (x2 - x1) == 0:
            continue
        slope = (y2 - y1) / (x2 - x1)

        if abs(x1 - x2) == abs(y1 - y2):
            delta = abs(x1 - x2) + 1
            for i in range(delta):
                if x1 > x2:
                    x = x1 - i
                else:
                    x = x1 + i

                if y1 > y2:
                    y = y1 - i
                else:
                    y = y1 + i

                grid[y][x] += 1

    num_overlaps = 0
    for line in grid:
        for l in line:
            if l >= 2:
                num_overlaps += 1 
    print(f"Result for Part 2: {num_overlaps}")

