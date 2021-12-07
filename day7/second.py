def calculateResult(data):
    mean = int(sum(data) / len(data))
    best_cost = -1
    for i in range(mean - 1, mean + 2):
        cost = 0
        temp = 0
        for position in data:
            temp = abs(position - i)
            cost += int(temp * (temp + 1) / 2)

        if best_cost == -1 or cost < best_cost:
            best_cost = cost

    return best_cost


def main():
    with open('data.txt') as f:
        lines = f.read().splitlines()

    data = list(map(int, lines[0].split(",")))

    print(calculateResult(data))


if __name__ == "__main__":
    main()
