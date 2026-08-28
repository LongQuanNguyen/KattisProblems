def main():
    n_char = input()
    string  = input()

    if "lv" in string:
        return 0

    if "l" in string:
        return 1

    if "v" in string:
        return 1

    return 2

if __name__ == "__main__":
    print(main())