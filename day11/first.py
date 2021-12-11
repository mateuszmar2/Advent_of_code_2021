flash_count = 0


def flash(y_flashed, x_flashed, size, data):
    global flash_count
    for y in range(y_flashed - 1, y_flashed + 2, 1):
        if y < 0 or y >= size:
            continue
        for x in range(x_flashed - 1, x_flashed + 2, 1):
            if x < 0 or x >= size:
                continue
            if data[y][x] != 10:
                data[y][x] += 1
            if data[y][x] == 10:
                data[y][x] += 1
                flash_count += 1
                flash(y, x, size, data)


def calculateResult(data, steps):
    global flash_count
    size = len(data)
    for s in range(steps):
        for y in range(size):
            for x in range(size):
                # print(data[y][x])
                if data[y][x] != 10:
                    data[y][x] += 1
                if data[y][x] == 10:
                    data[y][x] += 1
                    flash_count += 1
                    flash(y, x, size, data)
                    # print()
                    # for line in data:
                    #     print(line)

        for y in range(size):
            for x in range(size):
                if data[y][x] > 9:
                    data[y][x] = 0

        # print()
        # for line in data:
        #     print(line)

    return flash_count


def main():
    with open('data.txt') as f:
        lines = f.read().splitlines()

    data = []
    for line in lines:
        data += [list(map(int, line))]

    for line in data:
        print(line)

    print(calculateResult(data, 100))

    for line in data:
        print(line)


if __name__ == "__main__":
    main()
