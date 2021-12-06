def calculateResult(data, days):
    for day in range(days):
        data_len = len(data)
        for i in range(data_len - 1, -1, -1):
            if data[i] == 0:
                data[i] = 6
                data.append(8)
            else:
                data[i] -= 1

    return len(data)


def main():
    with open('data.txt') as f:
        lines = f.read().splitlines()

    data = list(map(int, lines[0].split(",")))

    print(calculateResult(data, 80))


if __name__ == "__main__":
    main()
