def main():
    inp = int(input())
    factors = []

    while True:
        factor = find_factor(inp)
        if factor != -1:
            factors.append(factor)
            inp = int(inp / factor)
        else:
            break
    print(len(factors))


def find_factor(number):
    for i in range(2, number + 1):
        if (number % i) == 0:
            # print(number, i)
            return i
    return -1


if __name__ == '__main__':
    main()