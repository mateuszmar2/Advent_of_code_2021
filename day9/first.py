def calculateResult(lines):
    total = 0
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
            total += int(lines[y][x]) + 1

    return total


def main():
    with open('data.txt') as f:
        lines = f.read().splitlines()

    print(calculateResult(lines))


if __name__ == "__main__":
    main()
