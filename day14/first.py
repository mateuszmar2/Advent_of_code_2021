def makeStep(template, rules):
    size = len(template)
    new_template = ""
    for i in range(size - 1):
        pair = template[i] + template[i + 1]
        for p in rules:
            if pair == p[0]:
                if i != size - 2:
                    new_template += pair[0] + p[1]
                else:
                    new_template += pair[0] + p[1] + pair[1]

    return new_template


def main():
    with open('data.txt') as f:
        lines = f.read().splitlines()

    template = lines[0]

    rules = lines[2:]

    for i, rule in enumerate(rules):
        rules[i] = rule.split(" -> ")

    for i in range(10):
        template = makeStep(template, rules)

    letters = {}
    for c in template:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1

    print(max(letters.values()) - min(letters.values()))


if __name__ == "__main__":
    main()
