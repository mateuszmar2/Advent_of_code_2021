def makeStep(x_pos, y_pos, x, y):
    if x > 0:
        x -= 1
    y -= 1
    x_pos += x
    y_pos += y
    return x_pos, y_pos, x, y


def checkVelocity(x, y, x_min, x_max, y_min, y_max):
    x_pos = x
    y_pos = y
    max_y = y
    while x_pos <= x_max and y_pos > y_min:
        x_pos, y_pos, x, y = makeStep(x_pos, y_pos, x, y)
        if y_pos > max_y:
            max_y = y_pos
        if x_min <= x_pos <= x_max and y_min <= y_pos <= y_max:
            return max_y
    return 0


def main():
    with open('data.txt') as f:
        lines = f.read()

    data = (lines[13:].split(", "))
    for i in range(2):
        data[i] = data[i][2:].split("..")

    x_min, x_max = list(map(int, data[0]))
    y_min, y_max = list(map(int, data[1]))
    max_y = 0
    for y in range(x_max * 3):
        for x in range(x_max):
            temp = checkVelocity(x, y, x_min, x_max, y_min, y_max)
            if (temp > max_y):
                max_y = temp

    print(max_y)


if __name__ == "__main__":
    main()
