def main():
    num_count = int(input())
    num_list = list(map(int, input().split()))

    occurrence = {}
    for num in num_list:
        if occurrence.get(num) is None:
            occurrence[num] = 1
        else:
            occurrence[num] += 1

    ways = 0

    key_list = list(occurrence.keys())
    for i, ai in enumerate(key_list):
        for j in range(i, len(key_list)):
            aj = key_list[j]
            ak =  ai + aj
            if occurrence.get(ak) is None:
                continue
            added_count = 0
            if ai == aj == ak:
                added_count = max(0, occurrence[ai] * (occurrence[aj]-1) * (occurrence[ak]-2))
            elif ai == aj != ak:
                added_count = occurrence[ai] * (occurrence[ai] - 1) * occurrence[ak]
            elif ai != aj and aj == ak:
                added_count = 2 * occurrence[ai] * occurrence[aj] * (occurrence[aj]-1)
            elif ai != aj and ai == ak:
                added_count = 2 * occurrence[ai] * occurrence[aj] * (occurrence[ai]-1)
            elif ai != aj and aj != ak and ai != ak:
                added_count = 2 * occurrence[ai] * occurrence[aj] * occurrence[ak]

            ways += added_count
            #print(ai, aj, ak, added_count)
    print(ways)

if __name__ == "__main__":
    main()