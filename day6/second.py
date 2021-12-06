def calculateResult(data, days):
    fish_cout = {i: data.count(i) for i in range(9)}

    for _ in range(days):
        temp = fish_cout[8]
        for key in reversed(fish_cout.keys()):
            if key == 0:
                fish_cout[8] = temp
                fish_cout[6] += temp
            else:
                temp2 = fish_cout[key - 1]
                fish_cout[key - 1] = temp
                temp = temp2

    return sum(fish_cout.values())


def main():
    with open('data.txt') as f:
        lines = f.read().splitlines()

    data = list(map(int, lines[0].split(",")))

    print(calculateResult(data, 256))


if __name__ == "__main__":
    main()
