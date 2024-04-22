def remove_negative(num_list):
    return_list = []
    for i in num_list:
        if i >= 0:
            return_list.append(i)
    return return_list


def collapse_zero(num_list):
    for i in num_list:
        if i != 0:
            return num_list

    if len(num_list) == 0:
        return num_list
    return [0]


def main():
    num1 = list(map(int, list(input())))
    num2 = list(map(int, list(input())))

    len1 = len(num1)
    len2 = len(num2)

    if len1 > len2:
        num2 = [0]*(len1 - len2) + num2
    elif len1 < len2:
        num1 = [0]*(len2 - len1) + num1

    for i in range(max(len1, len2)):
        if num1[i] > num2[i]:
            num2[i] = -1
        elif num1[i] < num2[i]:
            num1[i] = -1

    processed_num1 = collapse_zero(remove_negative(num1))
    processed_num2 = collapse_zero(remove_negative(num2))

    print(''.join(map(str, processed_num1)) if len(processed_num1) != 0 else 'YODA')
    print(''.join(map(str, processed_num2)) if len(processed_num2) != 0 else 'YODA')


if __name__ == '__main__':
    main()
