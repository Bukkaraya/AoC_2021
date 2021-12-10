from collections import deque


def get_adjacent_points(height_map, i, j):
    points = []
    locations = []

    if i - 1 >= 0:
        points.append(height_map[i - 1][j])
        locations.append((i - 1, j))
    if i + 1 < len(height_map):
        points.append(height_map[i + 1][j])
        locations.append((i + 1, j))

    if j - 1 >= 0:
        points.append(height_map[i][j - 1])
        locations.append((i, j - 1))
    if j + 1 < len(height_map[i]):
        points.append(height_map[i][j + 1])
        locations.append((i, j + 1))

    return points, locations


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        height_map = f.read().split("\n")

    height_map = [list(map(int, list(h))) for h in height_map]

    low_points = []
    low_point_locations = []

    for i in range(len(height_map)):
        for j in range(len(height_map[i])):
            current_point = height_map[i][j]
            points, _ = get_adjacent_points(height_map, i, j)
            points.append(current_point)

            if min(points) == current_point and points.count(
                    current_point) == 1:
                low_points.append(current_point)
                low_point_locations.append((i, j))

    basins = []
    for low_point in low_point_locations:
        basin_points = deque([low_point])
        basin_size = 0
        explored_points = set()

        while len(basin_points) != 0:
            i, j = basin_points.pop()
            if (i, j) in explored_points:
                continue

            explored_points.add((i, j))
            if height_map[i][j] != 9:
                basin_size += 1
                _, locations = get_adjacent_points(height_map, i, j)
                if locations:
                    basin_points.extend(locations)

        basins.append(basin_size)

    basins = sorted(basins, reverse=True)
    print(f"Result for Part 1: {sum(low_points) + len(low_points)}")
    print(f"Result for Part 2: {basins[0] * basins[1] * basins[2]}")
