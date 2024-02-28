original = [['A','B','C','D'],
            ['E','F','G','H'],
            ['I','J','K','L'],
            ['M','N','O','.']]

def main():
    original_dict = dict()
    for i in range(4):
        for j in range(4):
            if original[i][j] not in original_dict:
                original_dict[original[i][j]] = (i, j)
    #print(original_dict)

    input_array = []
    for i in range(4):
        inp = input()
        input_array.append(list(inp))
    #print(input_array)

    total_man_dist = 0
    for i in range(4):
        for j in range(4):
            if input_array[i][j] == '.':
                continue
            else:
                dx = abs((original_dict.get(input_array[i][j])[0]) - i)
                dy = abs((original_dict.get(input_array[i][j])[1]) - j)
                #print(input_array[i][j], dx, dy)
                total_man_dist += dx + dy

    print(total_man_dist)

if __name__ == '__main__':
    main()