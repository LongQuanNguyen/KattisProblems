def main():
    inp = float(input())

    # a^N = N
    if inp == 1:
        print(float(1))
    else:
        print(inp**(1/inp))


if __name__ == '__main__':
    main()