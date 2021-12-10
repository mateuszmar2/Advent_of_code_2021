def calculateResult(line, openings, closings):
    line_unclosed = []
    for c in line:
        if c in openings:
            line_unclosed.append(c)
            continue
        if not line_unclosed:
            return c

        found = False
        for i, opening in enumerate(openings):
            if line_unclosed[-1] == opening:
                if c == closings[i]:
                    line_unclosed.pop()
                    found = True
                    break
        # jeżeli coś jest źle
        if not found:
            return c
    return ""


def main():
    with open('data.txt') as f:
        lines = f.read().splitlines()

    openings = ["(", "[", "{", "<"]
    closings = [")", "]", "}", ">"]
    result = []
    for line in lines:
        result.append(calculateResult(line, openings, closings))

    total = 0
    points = [3, 57, 1197, 25137]
    for i, c in enumerate(closings):
        for cr in result:
            if cr == c:
                total += points[i]

    print(total)


if __name__ == "__main__":
    main()
