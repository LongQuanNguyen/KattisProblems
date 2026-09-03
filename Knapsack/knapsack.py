def inspect_matrix(matrix):
    for row in matrix:
        print(row)


def bottom_up_dp(optimal_val_table, item_weights, item_values, num_items, capacity):
    for i in range(1, num_items + 1):
        i_value = item_values[i - 1]
        i_weights = item_weights[i - 1]
        for c in range(capacity + 1):

            # Skip mean use prev row value
            skip_value = optimal_val_table[i - 1][c]

            if i_weights > c:
                optimal_val_table[i][c] = skip_value
            else:
                take_value = i_value + optimal_val_table[i - 1][c - i_weights]

                if take_value > skip_value:
                    optimal_val_table[i][c] = take_value
                else:
                    optimal_val_table[i][c] = skip_value


def get_optimal_item_indices(optimal_val_table, num_items, capacity, item_weights):
    i = num_items
    c = capacity
    indices = []

    while i > 0:
        if optimal_val_table[i][c] != optimal_val_table[i - 1][c]:
            indices.append(i - 1)
            c -= item_weights[i - 1]

        i -= 1

    return indices


def main():
    while True:
        try:
            item_weights = []
            item_values = []

            capacity, num_items = map(int, input().split())
            for idx in range(num_items):
                value, weight = map(int, input().split())
                item_weights.append(weight)
                item_values.append(value)

            optimal_val_table = [[0] * (capacity + 1) for _ in range(num_items + 1)]

            bottom_up_dp(optimal_val_table, item_weights, item_values, num_items, capacity)
            #inspect_matrix(optimal_val_table)
            indices = get_optimal_item_indices(optimal_val_table, num_items, capacity, item_weights)

            print(len(indices))
            print(" ".join(map(str, indices)))

        except EOFError:
            break

if __name__ == "__main__":
    main()