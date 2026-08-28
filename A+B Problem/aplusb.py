def string_to_int_list(str):
    return list(map(int, str.split()))


def get_freq_dict(int_list):
    freq_dict = {}
    for integer in int_list:
        if freq_dict.get(integer) is None:
            freq_dict[integer] = 1
        else:
            freq_dict[integer] += 1
    return freq_dict


def count_triples(int_list, length, freq_dict):
    total = 0

    for i in range(length):
        for j in range(length):
            if i == j:
                continue

            target_k = int_list[i] + int_list[j]

            number_of_k_choices = freq_dict.get(target_k, 0)
            if number_of_k_choices == 0:
                continue

            if int_list[i] == target_k:
                number_of_k_choices -= 1

            if int_list[j] == target_k:
                number_of_k_choices -= 1

            total += number_of_k_choices
    return total


def main():
    n = int(input())
    int_list = string_to_int_list(input())
    freq_dict = get_freq_dict(int_list)
    print(count_triples(int_list, n, freq_dict))

if __name__ == "__main__":
    main()