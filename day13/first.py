def fold(paper, fold_instruction):
    # for l in paper:
    #     print(l)

    size_x = len(paper[0])
    size_y = len(paper)
    if fold_instruction[0] == 'y':
        for i in range(size_x):
            for j in range(int(size_y / 2)):
                if paper[j][i] == '#':
                    continue
                if paper[size_y - 1 - j][i] == '#':
                    paper[j][i] = '#'
        paper = paper[:int(size_y / 2)]
    elif fold_instruction[0] == 'x':
        for i in range(int(size_x / 2)):
            for j in range(size_y):
                if paper[j][i] == '#':
                    continue
                if paper[j][size_x - 1 - i] == '#':
                    paper[j][i] = '#'
        for i in range(size_y):
            paper[i] = paper[i][:int(size_x / 2)]

    return paper


def main():
    with open('data.txt') as f:
        lines = f.read().splitlines()

    fold_instructions = []
    for line in reversed(lines):
        if not line:
            break
        fold_instructions.append(line.split()[-1].split('='))
    fold_instructions.reverse()

    coordinates = [0 for _ in range(len(lines) - len(fold_instructions) - 1)]
    for i, line in enumerate(lines):
        if not line:
            break
        coordinates[i] = list(map(int, line.split(',')))

    max_x = max(coordinates, key=lambda c: c[0])[0]
    max_y = max(coordinates, key=lambda c: c[1])[1]

    paper = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y in coordinates:
        paper[y][x] = '#'

    paper = fold(paper, fold_instructions[0])
    count = 0
    for l in paper:
        for v in l:
            if v == '#':
                count += 1

    print(count)


if __name__ == "__main__":
    main()
