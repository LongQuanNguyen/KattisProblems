def not_zero(x):
    if x != 0:
        return True
    else:
        return False


def left(array):
    new_array = []
    for row in array:
        new_row = list(filter(not_zero, row))
        if len(new_row) == 1:
            new_row += [0, 0, 0]
            new_array.append(new_row)
        else:
            for i in range(len(new_row)-1):
                if new_row[i] == new_row[i+1]:
                    new_row[i] = 2*new_row[i]
                    new_row[i+1] = 0
            newer_row = list(filter(not_zero, new_row))
            newer_row += [0]*(4-len(newer_row))
            new_array.append(newer_row)
    return new_array


def right(array):
    for row in array:
        row.reverse()
    new_array = left(array)
    for row in new_array:
        row.reverse()
    return new_array


def transpose(array):
    transposed = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            transposed[i][j] = array[j][i]
    return transposed


def up(array):
    return transpose(left(transpose(array)))


def down(array):
    return transpose(right(transpose(array)))


def main():
    init_arr = []
    for i in range(4):
        init_arr.append(list(map(int, input().split())))

    move = int(input())

    if move == 0:
        init_arr = left(init_arr)
    elif move == 2:
        init_arr = right(init_arr)
    elif move == 1:
        init_arr = up(init_arr)
    elif move == 3:
        init_arr = down(init_arr)
    else:
        pass

    for row in init_arr:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    main()