def makeStep(template_dict, rules, letters):
    new_template_dict = {}
    for key, value in template_dict.items():
        new_letter = rules[key]
        if new_letter in letters:
            letters[new_letter] += value
        else:
            letters[new_letter] = value

        for p in [key[0] + new_letter, new_letter + key[1]]:
            if p not in new_template_dict:
                new_template_dict[p] = value
            else:
                new_template_dict[p] += value

    return new_template_dict, letters


def main():
    with open('data.txt') as f:
        lines = f.read().splitlines()

    template = lines[0]

    rules = {}
    for line in lines[2:]:
        temp = line.split(" -> ")
        rules[temp[0]] = temp[1]

    template_dict = {}
    for i in range(len(template) - 1):
        pair = template[i] + template[i + 1]
        if pair in template_dict:
            template_dict[pair] += 1
        else:
            template_dict[pair] = 1

    letters = {l: template.count(l) for l in template}

    for i in range(40):
        template_dict, letters = makeStep(template_dict, rules, letters)

    print(max(letters.values()) - min(letters.values()))


if __name__ == "__main__":
    main()
