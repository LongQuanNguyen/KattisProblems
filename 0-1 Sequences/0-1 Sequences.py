def main():
    seq = input()
    ones = 0
    sequences = 1
    inversions = 0

    for bit in seq:
        if bit == "1":
            ones = (ones + sequences)
        if bit == "0":
            inversions = (inversions + ones)
        if bit == "?":
            inversions = (2 * inversions + ones)
            ones = (2 * ones + sequences)
            sequences = (2 * sequences)

    print(inversions)

if __name__ == "__main__":
    main()