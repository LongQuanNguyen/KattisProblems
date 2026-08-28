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


def count_triples(freq_dict):
    ways = 0
    dict_list = list(freq_dict.items())

    for dict_idx, (value_i, freq_i) in enumerate(dict_list):
        for value_j, freq_j in dict_list[dict_idx:]:
            value_k = value_i + value_j

            choices_i = freq_i
            choices_j = freq_j
            choices_k = freq_dict.get(value_k, 0)

            if choices_k == 0:
                continue

            if value_i == value_j:
                choices_j -= 1

            if value_k == value_i:
                choices_k -= 1

            if value_k == value_j:
                choices_k -= 1

            if choices_j <= 0 or choices_k <= 0:
                continue

            if value_i != value_j:
                ways += 2 * choices_i * choices_j * choices_k
            else:
                ways += choices_i * choices_j * choices_k

    return ways


def main():
    n = int(input())
    int_list = string_to_int_list(input())
    freq_dict = get_freq_dict(int_list)
    print(count_triples(freq_dict))

if __name__ == "__main__":
    main()