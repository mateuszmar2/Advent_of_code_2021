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
            return ""

    missing = []
    # w line_unclosed pozostała część, która nie była zamknięta
    for c in line_unclosed:
        for i, opening in enumerate(openings):
            if(c == opening):
                missing.insert(0, closings[i])
                break
    return missing


def main():
    with open('data.txt') as f:
        lines = f.read().splitlines()

    total = []
    openings = ["(", "[", "{", "<"]
    closings = [")", "]", "}", ">"]
    result = []
    for line in lines:
        result.append(calculateResult(line, openings, closings))
        # jeśli linia jest błędna
        if result[-1] == "":
            continue
        # jeśli otrzymano wygenerowane domknięcia
        temp = 0
        for c in result[-1]:
            for i, closing in enumerate(closings):
                if c == closing:
                    temp *= 5
                    temp += i + 1
                    break
        total.append(temp)

    total.sort()
    print(total[int(len(total)/2)])


if __name__ == "__main__":
    main()
