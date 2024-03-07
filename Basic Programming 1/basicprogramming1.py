def main():
    inp = input()
    arr_len, t = map(int, inp.split())
    #print(arr_len, t)

    inp = input()
    array = list(map(int, inp.split()))
    #print(array)

    if t == 1:
        print(7)
    elif t == 2:
        if array[0] > array[1]:
            print("Bigger")
        elif array[0] == array[1]:
            print("Equal")
        else:
            print("Smaller")
    elif t == 3:
        print(sorted(array[:3])[1])
    elif t == 4:
        print(sum(array))
    elif t == 5:
        print(sum(filter(lambda x: x % 2 == 0, array)))
    elif t == 6:
        array = list(map(lambda x: x % 26 + 97, array))
        print(''.join(list(map(chr, array))))
    elif t == 7:
        visited = [False]*arr_len
        current = 0
        while True:
            if current >= arr_len:
                print("Out")
                break

            if visited[current]:
                print("Cyclic")
                break

            if current == arr_len - 1:
                print("Done")
                break

            visited[current] = True
            current = array[current]
    else:
        pass


if __name__ == "__main__":
    main()
