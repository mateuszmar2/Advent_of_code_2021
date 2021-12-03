# program wczytuje dane do listy lines, dzięki splitlines() pomija znaki białe
# funkcja obliczająca wynik dla zadanego parametru
def calculate(oxygen, lines):
    tab = list(lines)
    position = 0

    # dopóki nie uzyskamy wyniku
    while len(tab) != 1:
        zero_count = 0
        one_count = 0
        # wyliczenie ilości zer i jedynek na danej pozycji
        for line in tab:
            if line[position] == '0':
                zero_count += 1
            elif line[position] == '1':
                one_count += 1

        # jeżeli obliczany jest tlen
        if oxygen:
            more = '0' if zero_count > one_count else '1'
        # jeżeli obliczane jest co2
        else:
            more = '0' if zero_count <= one_count else '1'
        tab = [
            item for item in tab if item[position] == more
        ]
        position += 1

    return int(tab[0], 2)


def main():
    with open('sample_data.txt') as f:
        lines = f.read().splitlines()

    oxygen = calculate(True, lines)
    co2 = calculate(False, lines)
    print(oxygen * co2)


if __name__ == "__main__":
    main()
