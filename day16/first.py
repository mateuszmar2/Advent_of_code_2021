def sumPacketsVersions(bin_string):
    if len(bin_string) < 11:
        return 0
    version_sum = 0
    version = int(bin_string[:3], base=2)
    type_id = int(bin_string[3:6], base=2)
    version_sum += version

    if type_id == 4:
        x = 6 + 5
        literal = bin_string[x - 5:x]
        while literal[0] == '1':
            x += 5
            literal = bin_string[x - 5:x]
        if x < len(bin_string):
            version_sum += sumPacketsVersions(bin_string[x:])
        return version_sum

    length_type_id = int(bin_string[6], base=2)
    if length_type_id == 0:
        total_length = int(bin_string[7:22], base=2)
        version_sum += sumPacketsVersions(bin_string[22:22 + total_length])
        version_sum += sumPacketsVersions(bin_string[22 + total_length:])
    else:
        version_sum += sumPacketsVersions(bin_string[18:])

    return version_sum


def main():
    with open('data.txt') as f:
        line = f.read()

    bin_string = ""
    for c in line:
        bin_string += format(int(c, base=16), '04b')

    print(sumPacketsVersions(bin_string))


if __name__ == "__main__":
    main()
