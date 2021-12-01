# program wczytuje dane do listy lines, inc_cout zlicza ilość zwiększeń głębokości
# pętla for przegląda kolejno każdą głębokość, pierwszy obieg pętli jest pomijany
with open('data.txt') as f:
    lines = f.read().splitlines()

lines_int = list(map(int, lines))

inc_count = selector = 0
sum_table = [0, 0, 0, 0]
sum_table[0] = sum(lines_int[:3])
sum_table[1] = sum(lines_int[1:3])
sum_table[2] = lines_int[2]

for x in lines_int[3:-2]:
    for y in range(0, 4):
        if y == selector:
            continue
        sum_table[y] += x

    if sum_table[(selector + 1) % 4] > sum_table[selector]:
        inc_count += 1
    sum_table[selector] = 0
    selector = (selector + 1) % 4

sum_table[(selector + 1) % 4] += lines_int[len(lines_int) - 2]
sum_table[(selector + 2) % 4] += lines_int[len(lines_int) - 2]
if sum_table[(selector + 1) % 4] > sum_table[selector]:
    inc_count += 1
selector = (selector + 1) % 4

sum_table[selector + 1] += lines_int[len(lines_int) - 1]
if sum_table[(selector + 1) % 4] > sum_table[selector]:
    inc_count += 1

print(inc_count)
