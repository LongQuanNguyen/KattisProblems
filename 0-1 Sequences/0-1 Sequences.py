def main():
    seq = input()
    ones = 0
    sequences = 1
    inversions = 0
    modulus = 10**9 +7

    for bit in seq:
        if bit == "1":
            ones = (ones + sequences) % modulus
        if bit == "0":
            inversions = (inversions + ones) % modulus
        if bit == "?":
            inversions = (2 * inversions + ones) % modulus
            ones = (2 * ones + sequences) % modulus
            sequences = (2 * sequences) % modulus

    print(inversions)

if __name__ == "__main__":
    main()