from queue import PriorityQueue
from dataclasses import dataclass, field


@dataclass(order=True)
class QElem:
    dist: int
    point: field(compare=False)


def findPath(data):
    size = len(data)
    distance = [[float("inf") for _ in range(size)]for _ in range(size)]

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

    print(findPath(data))


if __name__ == "__main__":
    main()
