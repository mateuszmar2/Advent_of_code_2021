# program wczytuje dane do listy lines, dzięki splitlines() pomija znaki białe
with open('sample_data.txt') as f:
    lines = f.read().splitlines()

gamma_bin = ""
epsilon_bin = ""
tab_zeros = [0 for _ in lines]
tab_ones = [0 for _ in lines]

# pętla licząca ilość zer i jedynek
for line in lines:
    for x in range(len(line)):
        if line[x] == '0':
            tab_zeros[x] += 1
        elif line[x] == '1':
            tab_ones[x] += 1

# pętla tworząca liczby binarne zależnie od ilości zer i jedynek na danej pozycji
for x in range(len(lines)):
    if tab_zeros[x] < tab_ones[x]:
        gamma_bin += '1'
        epsilon_bin += '0'
    elif tab_zeros[x] > tab_ones[x]:
        gamma_bin += '0'
        epsilon_bin += '1'

print(int(gamma_bin, 2) * int(epsilon_bin, 2))
