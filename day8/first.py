def calculateResult(data):
    count = 0
    for line in data:
        for s in line[-4:]:
            if len(s) in (2, 3, 4, 7):
                count += 1

    return count


def main():
    with open('data.txt') as f:
        lines = f.read().splitlines()

    data = [line.split() for line in lines]
    print(calculateResult(data))


if __name__ == "__main__":
    main()
