def count_walk(x, y, remaining_steps):
    if remaining_steps == 0:
        if (x, y) == (0, 0):
            return 1
        else:
            return 0

    total_walks = 0

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, -1),
        (-1, 1)
    ]
    for dx, dy in directions:
        total_walks += count_walk(x + dx, y + dy, remaining_steps - 1)

    return  total_walks

def main():
    n = int(input())
    for i in range(0,n):
        steps = int(input())
        print(count_walk(0, 0, steps))

if __name__ == "__main__":
    main()


