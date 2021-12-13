def calculateResult(edges):
    paths = [['start', node] for node in edges['start']]

    count = 0
    while paths:
        for path in paths:
            for node in edges[path[-1]]:
                if node == 'start':
                    continue
                elif node == 'end':
                    count += 1
                elif node not in path or node.isupper():
                    paths.append([*path, node])
            paths.remove(path)

    return count


def main():
    with open('data.txt') as f:
        lines = f.read().splitlines()

    data = [0 for _ in lines]
    for i, line in enumerate(lines):
        data[i] = line.split('-')

    edges = {}
    for i, edge in enumerate(data):
        if edge[0] not in edges:
            edges[edge[0]] = [edge[1]]
        else:
            edges[edge[0]].append(edge[1])
        if edge[1] not in edges:
            edges[edge[1]] = [edge[0]]
        else:
            edges[edge[1]].append(edge[0])

    print(calculateResult(edges))


if __name__ == "__main__":
    main()
