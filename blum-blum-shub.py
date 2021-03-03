
import argparse


def bbs(x, y, seed, number_of_bits):
    n = x * y

    assert (1 < seed < n)
    assert (seed % x != 0)
    assert (seed % y != 0)

    x = seed
    bits = ""
    for _ in range(number_of_bits):
        x = x * x % n
        b = x % 2
        bits += str(b)
    print(bits)


def main():
    parser = argparse.ArgumentParser(description='Runs the blum blum shub generator using two primes x and y, '
                                                 'a seed and the desired number of bits specified.')
    parser.add_argument('x', metavar='x', type=int,
                        help='preferably a large prime number')
    parser.add_argument('y', metavar='y', type=int,
                        help='preferably a large prime number')
    parser.add_argument('seed', metavar='seed', type=int,
                        help='a seed for the generator to start computation with')
    parser.add_argument('n', metavar='n', type=int,
                        help='desired number of bits')

    args = parser.parse_args()
    bbs(args.x, args.y, args.seed, args.n)


if __name__ == '__main__':
    main()
