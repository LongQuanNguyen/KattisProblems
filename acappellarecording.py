def main():
    n, d = map(int, input().split())
    notes = [int(input()) for _ in range(n)]

    notes_nodup = sorted(list(set(notes)))
    # print(n, d, notes_nodup)

    if d == 0:
        print(len(notes_nodup))
    else:
        count = 1
        current = notes_nodup[0]
        for i in notes_nodup:
            if i > current + d:
                current = i
                count += 1
        print(count)


if __name__ == '__main__':
    main()
