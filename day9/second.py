def searchForBasin(data, coordinates):
    basin_y, basin_x = coordinates
    basin_number = data[basin_y][basin_x]
    size = 1
    k = 0
    while True:
        k += 1
        count = 0
        for y in range(basin_y - k, basin_y + k + 1):
            if y < 0 or y >= len(data):
                continue
            for x in range(basin_x - k, basin_x + k + 1):
                if x < 0 or x >= len(data[0]):
                    continue
                value = int(data[y][x])
                if value == -1:
                    continue
                if y == basin_y - k or y == basin_y + k:
                    if x == basin_x - k or basin_x + k:
                        continue
                neighbours = [
                    data[y - 1][x] if y - 1 >= 0 else -1,
                    data[y + 1][x] if y + 1 < len(data) else -1,
                    data[y][x - 1] if x - 1 >= 0 else -1,
                    data[y][x + 1] if x + 1 < len(data[0]) else -1,
                ]
                if basin_number in neighbours and data[y][x] == 0:
                    data[y][x] = basin_number
                    size += 1
                    count += 1
        if count == 0:
            break

    return size


def calculateResult(lines):
    low_points = []
    basin_sizes = []
    max_x = len(lines[0])
    max_y = len(lines)

    for y in range(max_y):
        for x in range(max_x):
            if x - 1 >= 0:
                if lines[y][x - 1] <= lines[y][x]:
                    continue
            if x + 1 < max_x:
                if lines[y][x + 1] <= lines[y][x]:
                    continue
            if y - 1 >= 0:
                if lines[y - 1][x] <= lines[y][x]:
                    continue
            if y + 1 < max_y:
                if lines[y + 1][x] <= lines[y][x]:
                    continue
            # jeżeli jest mniejsza niż wszytkie istniejące, otaczające wartości
            low_points.append([y, x])

    data = []
    for line in lines:
        data += [list(map(int, line))]

    for y, row in enumerate(data):
        for x, val in enumerate(row):
            if val == 9:
                data[y][x] = -1
            else:
                data[y][x] = 0

    for i, coordinate in enumerate(low_points, 1):
        y, x = coordinate
        data[y][x] = i

    for coordinates in low_points:
        basin_sizes.append(searchForBasin(data, coordinates))
    basin_sizes.sort()

    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]


def main():
    with open('data.txt') as f:
        lines = f.read().splitlines()

    print(calculateResult(lines))


if __name__ == "__main__":
    main()
