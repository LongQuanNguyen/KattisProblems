def get_mapped_char():
    char_dict = {}
    for i in range(48,58,1):
        char_dict[chr(i)] = i - 48
    for i in range(97, 123, 1):
        char_dict[chr(i)] = i - 87
    for i in range(65, 91, 1):
        char_dict[chr(i)] = i - 29
    return char_dict

def get_decimal_val(represent_string, base, mapped_value):
    value = 0
    reverse_string = represent_string[::-1]
    for i, char in enumerate(reverse_string):
        digit = mapped_value[char]
        if digit >= base:
            return None
        value += digit * base ** i
    return value

def main():
    total_pairs = int(input())
    mapped_char = get_mapped_char()

    for i in range(total_pairs):
        A, B = input().split()

        A_values = {}
        for base in range(2, 7501, 1):
            A_val = get_decimal_val(A, base, mapped_char)
            if A_val is not None:
                A_values[A_val] = base
        found = False
        for base in range(2, 7501, 1):
            B_val = get_decimal_val(B, base, mapped_char)
            if B_val in A_values:
                found = True
                print(B_val, A_values.get(B_val), base)
                break

        if not found:
            print("CANNOT MAKE EQUAL")

if __name__ == "__main__":
    main()