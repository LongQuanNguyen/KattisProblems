def main():
    while True:
        try:
            item_weight= []
            value_weight_ratio = {}

            capacity, n = map(int, input().split())
            for idx in range(n):
                value, weight = map(int, input().split())
                item_weight.append(weight)
                value_weight_ratio[idx] = value / weight

            sorted_value_weight_desc = dict(sorted(value_weight_ratio.items(), key=lambda item: item[1], reverse=True))
            chosen_indices = []
            total_weight = 0
            for idx, ratio in sorted_value_weight_desc.items():
                if item_weight[idx] + total_weight <= capacity:
                    chosen_indices.append(idx)
                    total_weight += item_weight[idx]

            print(len(chosen_indices))
            print(" ".join(map(str, chosen_indices)))

        except EOFError:
            break

if __name__ == "__main__":
    main()