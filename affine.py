mtrx = [
    0b11110001,
    0b11100011,
    0b11000111,
    0b10001111,
    0b00011111,
    0b00111110,
    0b01111100,
    0b11111000,
]


def affine(byte):
    output = []
    for row in mtrx:
        row_s = bin(row & byte).lstrip("-0b")
        output.insert(0, str(row_s.count('1') % 2))
    return int("".join(output), 2) ^ 0b01100011


def main():
    print("S(29) is", hex(affine(0xA8)).lstrip("-0x").zfill(2).upper())
    print("S(F3) is", hex(affine(0x34)).lstrip("-0x").zfill(2).upper())


if __name__ == "__main__":
    main()
