def main():
    inp = int(input())
    factors = []

    while True:
        factor = find_factor(inp)
        if factor != 1:
            factors.append(factor)
            inp = int(inp / factor)
        else:
            break
    print(len(factors))


def find_factor(number):
    sq_root_number = int(number**(1/2))
    for i in range(2, sq_root_number + 1):
        if (number % i) == 0:
            # print(number, i, sq_root_number)
            return i
    return number


if __name__ == '__main__':
    main()