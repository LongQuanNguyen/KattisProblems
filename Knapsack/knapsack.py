def maximize_value(idx, capacity, num_items, item_weights, item_values, cache):
    if idx == num_items or capacity == 0:
        cache[(idx, capacity)] = 0, False
        return 0

    if (idx, capacity) in cache:
        return cache[(idx, capacity)][0]

    skip = maximize_value(idx + 1, capacity, num_items, item_weights, item_values, cache)

    if item_weights[idx] > capacity:
        cache[(idx, capacity)] = skip, False
        return skip

    take = item_values[idx] + maximize_value(idx + 1, capacity - item_weights[idx], num_items, item_weights, item_values, cache)
    cache[(idx, capacity)] = max(take, skip), take >= skip
    return cache[(idx, capacity)][0]


def reconstruct_indices_of_optimal(capacity, num_items, cache, item_weights):
    chosen_indices = []
    i = 0
    cap = capacity
    while i < num_items:
        value, is_taken = cache[(i, cap)]

        if is_taken:
            chosen_indices.append(i)
            cap -= item_weights[i]

        i += 1
    return  chosen_indices


def main():
    while True:
        try:
            item_weights = []
            item_values = []
            cache = {}

            capacity, num_items = map(int, input().split())
            for idx in range(num_items):
                value, weight = map(int, input().split())
                item_weights.append(weight)
                item_values.append(value)

            maximize_value(0, capacity, num_items, item_weights, item_values, cache)

            indices = reconstruct_indices_of_optimal(capacity, num_items, cache, item_weights)
            print(len(indices))
            print(" ".join(map(str, indices)))

        except EOFError:
            break

if __name__ == "__main__":
    main()