def makeStep(x_pos, y_pos, x, y):
    if x > 0:
        x -= 1
    y -= 1
    x_pos += x
    y_pos += y
    return x_pos, y_pos, x, y


def checkVelocity(x, y, x_min, x_max, y_min, y_max):
    x_pos = 0
    y_pos = 0
    while x_pos <= x_max and y_pos > y_min:
        x_pos, y_pos, x, y = makeStep(x_pos, y_pos, x, y)
        if x_min <= x_pos <= x_max and y_min <= y_pos <= y_max:
            return True
    return False


def main():
    with open('data.txt') as f:
        lines = f.read()

    data = (lines[13:].split(", "))
    for i in range(2):
        data[i] = data[i][2:].split("..")

    x_min, x_max = list(map(int, data[0]))
    y_min, y_max = list(map(int, data[1]))
    count = 0
    scale = 3
    for x in range(x_max * scale):
        for y in range(y_min * scale, - y_max * scale, 1):
            if (checkVelocity(x, y, x_min, x_max, y_min, y_max)):
                count += 1

    print(count)


if __name__ == "__main__":
    main()
