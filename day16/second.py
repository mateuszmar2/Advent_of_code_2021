class Packet:
    def __init__(self):
        self.version = None
        self.type_id = None
        self.length_type_id = None
        self.length = None
        self.value = None
        self.subpackets = []

    def __str__(self) -> str:
        if self.type_id == 4:
            return f"Packet(version={self.version}, type_id={self.type_id}, value={self.value})"
        else:
            return f"Packet(version={self.version}, type_id={self.type_id}, length_type_id={self.length_type_id}, self_length={self.length}, subpackets={self.subpackets})"

    __repr__ = __str__

    def decode(self, bin_string):
        self.version = int(bin_string[:3], base=2)
        self.type_id = int(bin_string[3:6], base=2)
        bin_string = bin_string[6:]

        if self.type_id == 4:
            bin_string = self.calculateLiteral(bin_string)
        else:
            self.length_type_id = int(bin_string[0], base=2)
            bin_string = bin_string[1:]
            if self.length_type_id == 0:
                self.length = int(bin_string[:15], base=2)
                bin_string = bin_string[15:]
            else:
                self.length = int(bin_string[:11], base=2)
                bin_string = bin_string[11:]

            bin_string = self.calculateOperator(bin_string)
        return bin_string

    def calculateLiteral(self, bin_string):
        x = 5
        literal = bin_string[x - 5:x]
        literal_string = literal[1:]
        while literal[0] == '1':
            x += 5
            literal = bin_string[x - 5:x]
            literal_string += literal[1:]
        bin_string = bin_string[x:]
        self.value = int(literal_string, base=2)
        return bin_string

    def calculateOperator(self, bin_string):
        if self.length_type_id == 0:
            bin_string_cpy = bin_string[:self.length]
            bin_string = bin_string[self.length:]
            while bin_string_cpy:
                new_packet = Packet()
                bin_string_cpy = new_packet.decode(bin_string_cpy)
                self.subpackets.append(new_packet)
        else:
            while len(self.subpackets) < self.length:
                new_packet = Packet()
                bin_string = new_packet.decode(bin_string)
                self.subpackets.append(new_packet)
        return bin_string

    def versionSum(self):
        total_sum = self.version
        if self.type_id != 4:
            total_sum += sum(sp.versionSum() for sp in self.subpackets)
        return total_sum

    def calculateValue(self):
        if self.type_id == 0:
            return sum(sp.calculateValue() for sp in self.subpackets)
        elif self.type_id == 1:
            total_product = 1
            for sp in self.subpackets:
                total_product *= sp.calculateValue()
            return total_product
        elif self.type_id == 2:
            return min(sp.calculateValue() for sp in self.subpackets)
        elif self.type_id == 3:
            return max(sp.calculateValue() for sp in self.subpackets)
        elif self.type_id == 4:
            return self.value
        elif self.type_id == 5:
            return self.subpackets[0].calculateValue() > self.subpackets[1].calculateValue()
        elif self.type_id == 6:
            return self.subpackets[0].calculateValue() < self.subpackets[1].calculateValue()
        elif self.type_id == 7:
            return self.subpackets[0].calculateValue() == self.subpackets[1].calculateValue()


def main():
    with open('data.txt') as f:
        line = f.read()

    bin_string = ""
    for c in line:
        bin_string += format(int(c, base=16), '04b')

    packet = Packet()
    packet.decode(bin_string)
    # print(packet.versionSum())
    print(packet.calculateValue())


if __name__ == "__main__":
    main()
