from queue import PriorityQueue
from dataclasses import dataclass, field


@dataclass(order=True)
class QElem:
    dist: int
    point: field(compare=False)


def findPath(data):
    size = len(data)
    distance = [[float("inf") for _ in range(size)] for _ in range(size)]

    distance[0][0] = 0

    q = PriorityQueue()
    q.put(QElem(distance[0][0], [0, 0]))

    while not q.empty():
        elem = q.get()
        dist = elem.dist
        base_y, base_x = elem.point
        for y, x in [[base_y - 1, base_x], [base_y, base_x - 1], [base_y, base_x + 1], [base_y + 1, base_x]]:
            if 0 <= y < size and 0 <= x < size:
                weight = dist + data[y][x]
                if distance[y][x] > weight:
                    distance[y][x] = weight
                    q.put(QElem(weight, [y, x]))

    return distance[size - 1][size - 1]


def main():
    with open('data.txt') as f:
        lines = f.read().splitlines()

    data = []
    for line in lines:
        data.append(list(map(int, line)))

    size = len(data)
    data_full = [[0 for _ in range(size * 5)] for _ in range(size * 5)]

    for y, row in enumerate(data_full[:size]):
        i = -1
        for x, val in enumerate(row):
            x_data = x % size
            if x_data == 0:
                i += 1
            data_full[y][x] = (data[y][x_data] + i - 1) % 9 + 1

    size_full = len(data_full)
    i = 0
    for y, row in enumerate(data_full[size:], start=size):
        y_data = y % size
        if y_data == 0:
            i += 1
        for x, val in enumerate(row):
            x_data = x % size_full
            data_full[y][x] = (data_full[y_data][x_data] + i - 1) % 9 + 1

    print(findPath(data_full))


if __name__ == "__main__":
    main()
