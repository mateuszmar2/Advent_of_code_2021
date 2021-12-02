# program wczytuje dane do listy lines, dzięki splitlines() pomija znaki białe
# pętla sprawdza jakie słowo napotkano i zwiększa lub zmniejsza pozycję lub głębokość
with open('data.txt') as f:
    lines = f.read().splitlines()

depth = position = 0

for line in lines:
    if line[0] == 'f':
        position += int(line[-1])
    elif line[0] == 'd':
        depth += int(line[-1])
    elif line[0] == 'u':
        depth -= int(line[-1])

print(depth * position)
