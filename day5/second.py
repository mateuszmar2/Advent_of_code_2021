# funkcja sprawdza czy linia jest pionowa, pozioma czy skośna i inkrementuje wartości o danych współrzędnych w board
def calculateResult(coordinates):
    max_val = max(max(l) for l in coordinates)
    board = [[0 for _ in range(max_val + 1)] for _ in range(max_val + 1)]
    for x1, y1, x2, y2 in coordinates:
        # jeżeli y się nie zmienia
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                board[y1][x] += 1

        # jeżeli x się nie zmienia
        elif x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                board[y][x1] += 1

        # jeżeli oba się zmieniają
        else:
            if x1 > x2:
                x_range = x2 - 1
                cx = -1
            else:
                x_range = x2 + 1
                cx = 1
            y = y1
            if y1 > y2:
                cy = -1
            else:
                cy = 1
            for x in range(x1, x_range, cx):
                board[y][x] += 1
                y += cy

    greater_count = 0
    for line in board:
        greater_count += len([1 for i in line if i > 1])
    return greater_count


def main():
    with open('data.txt') as f:
        lines = f.read().splitlines()

    coordinates = [0 for _ in lines]
    for i, line in enumerate(lines):
        coordinates[i] = line.replace(" -> ", ",")
        coordinates[i] = list(map(int, coordinates[i].split(",")))

    print(calculateResult(coordinates))


if __name__ == "__main__":
    main()
