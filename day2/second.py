# program wczytuje dane do listy lines, dzięki splitlines() pomija znaki białe
# pętla sprawdza jakie słowo napotkano i zwiększa lub zmniejsza pozycję, głębokość lub aim
with open('data.txt') as f:
    lines = f.read().splitlines()

depth = position = aim = 0

for line in lines:
    digit = int(line[-1])
    if line[0] == 'f':
        position += digit
        depth += aim * digit
    elif line[0] == 'd':
        aim += digit
    elif line[0] == 'u':
        aim -= digit

print(depth * position)
