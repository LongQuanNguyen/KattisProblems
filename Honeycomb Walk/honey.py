def count_walk(x, y, remaining_steps, dict_cache):
    state = (x, y, remaining_steps)

    if state in dict_cache:
        return dict_cache[state]

    if remaining_steps == 0:
        if (x, y) == (0, 0):
            result = 1
        else:
            result = 0

        dict_cache[state] = result
        return result

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
        total_walks += count_walk(x + dx, y + dy, remaining_steps - 1, dict_cache)

    return  total_walks

def main():
    n = int(input())
    dict_cache = {}
    for i in range(0,n):
        steps = int(input())
        print(count_walk(0, 0, steps, dict_cache))

if __name__ == "__main__":
    main()