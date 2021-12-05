# funkcja sprawdza czy linia jest pionowa czy pozioma i inkrementuje wartości o danych współrzędnych w board
def calculateResult(coordinates):
    max_val = max(max(l) for l in coordinates)
    # tablica na wartości o danych współrzędnych o wielkości największej współrzędnej
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

    greater_count = 0
    for line in board:
        greater_count += sum(1 for i in line if i > 1)
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
