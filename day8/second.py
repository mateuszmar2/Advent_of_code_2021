def calculateDigits(line):
    digits_list = ["" for _ in range(10)]
    list_235 = ["" for _ in range(3)]
    list_069 = ["" for _ in range(3)]
    i = 0
    j = 0
    for s in line:
        # sprawdzenie 1
        if len(s) == 2:
            digits_list[1] = s
        # sprawdzenie 7
        elif len(s) == 3:
            digits_list[7] = s
        # sprawdzenie 4
        elif len(s) == 4:
            digits_list[4] = s
        # sprawdzenie 8
        elif len(s) == 7:
            digits_list[8] = s
        # sprawdzenie 2, 3, 5
        elif len(s) == 5:
            list_235[i] = s
            i += 1
        # sprawdzenie 0, 6, 9
        elif len(s) == 6:
            list_069[j] = s
            j += 1

    for digit in list_069:
        for c in digits_list[4]:
            # jeżeli nie jest 9
            if c not in digit:
                # jeżeli to 0
                if c not in digits_list[1]:
                    digits_list[0] = digit
                # jeżeli to 6
                else:
                    digits_list[6] = digit
    # znalezienie 9
    for digit in list_069:
        if digit != digits_list[0] and digit != digits_list[6]:
            digits_list[9] = digit

    # znalezienie 3
    for digit in list_235:
        if digits_list[1][0] in digit and digits_list[1][1] in digit:
            digits_list[3] = digit

    # znalezienie 2
    for digit in list_235:
        if digit == digits_list[3]:
            continue
        for c in digits_list[4]:
            if c not in digit:
                if c not in digits_list[1]:
                    digits_list[2] = digit

    # znalezienie 5
    for digit in list_235:
        if digit == digits_list[3]:
            continue
        if digit != digits_list[2]:
            digits_list[5] = digit

    return {frozenset(digits_list[i]): i for i in range(10)}


def calculateResult(line):
    digits_map = calculateDigits(line[:10])
    output = ""
    x = 0
    for digit in line[-4:]:
        output += str(digits_map[frozenset(digit)])

    return int(output)


def main():
    with open('data.txt') as f:
        lines = f.read().splitlines()

    data = []
    for line in lines:
        data.append(line.split(" "))

    sum = 0
    for line in data:
        sum += calculateResult(line)

    print(sum)


if __name__ == "__main__":
    main()
