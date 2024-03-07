def main():
    while True:
        try:
            first, second = list(map(int, input().split()))
            print(abs(first - second))
        except EOFError:
            break


if __name__ == '__main__':
    main()
