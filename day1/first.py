# program wczytuje dane do listy lines, inc_cout zlicza ilość zwiększeń sum trójek głębokości
# pętla for przegląda kolejno każdą głębokość, pierwszy obieg pętli jest pomijany
with open('data.txt') as f:
    lines = f.readlines()

inc_count = 0
prev = lines[0].rstrip()  # rstrip usuwa znaki białe z końca linii
for line in lines:
    if line == lines[0]:
        continue
    line = line.rstrip()
    if int(line) > int(prev):
        inc_count += 1
    prev = line

print(inc_count)
