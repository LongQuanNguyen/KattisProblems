def main():
    while True:
        n, m = map(int, input().split())

        if n == 0 and m == 0:
            break

        calls = []

        for _ in range(n):
            src, dst, start, dur = map(int, input().split())
            calls.append((start, start + dur))

        for _ in range(m):
            tap_start, tap_duration = map(int, input().split())
            tap_end = tap_start + tap_duration

            count = 0

            for call_start, call_end in calls:
                if call_start < tap_end and call_end > tap_start:
                    count += 1

            print(count)

if __name__ == "__main__":
    main()