from os import confstr
from statistics import median


def calculateResult(data):
    cost = 0
    for position in data:
        cost += abs(position - median(data))

    return (int(cost))


def main():
    with open('data.txt') as f:
        lines = f.read().splitlines()

    data = list(map(int, lines[0].split(",")))
    print(calculateResult(data))


if __name__ == "__main__":
    main()
