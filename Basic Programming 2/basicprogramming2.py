def main():
    arr_len, t = list(map(int, input().split()))
    #print(arr_len, t)

    arr = list(map(int, input().split()))
    #print(arr)

    if t == 1:
        no_dup = list(set(arr))
        found = False
        for i, number in enumerate(no_dup[:-1]):
            complementary = 7777 - number
            if complementary in no_dup:
                found = True
                break
        print("Yes" if found else "No")
    elif t == 2:
        if arr_len != len(set(arr)):
            print("Contains duplicate")
        else:
            print("Unique")
    elif t == 3:
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        most_repeated = max(freq, key=freq.get)
        print(most_repeated if freq[most_repeated] >= arr_len//2 + 1 else -1)
    elif t == 4:
        arr.sort()
        #print(arr)
        if arr_len % 2 == 1:
            print(arr[arr_len//2])
        else:
            print(arr[int(arr_len/2) - 1], arr[int(arr_len/2)])
    elif t == 5:
        filtered = [x for x in arr if 100 <= x <= 999]
        filtered.sort()
        print(' '.join(map(str, filtered)))

    else:
        pass


if __name__ == "__main__":
    main()