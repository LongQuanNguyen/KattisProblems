def main():
    num_ppl = int(input())
    potential_matrix = []
    pair_potential = {}
    triangle_potential = {}

    for i in range(num_ppl):
        potential_matrix.append(list(map(int, input().split())))
    # print(potential_matrix)

    for i in range(num_ppl):
        for j in range(i, num_ppl):
            if potential_matrix[i][j] > 0:
                pair_potential[(i + 1, j + 1)] = potential_matrix[i][j]
    # print(pair_potential)

    for (i, j) in pair_potential.keys():
        for (a, b) in pair_potential.keys():
            # print(i, j, a, b)
            if i == a and j != b:
                second_third = pair_potential[(min(j, b), max(j, b))] if (min(j, b), max(j, b)) in pair_potential else 0
                triangle_potential[(i, min(j, b), max(j, b))] = pair_potential[(i, j)] * pair_potential[(a, b)] * second_third
            elif j == a:
                first_third = pair_potential[(min(i, b), max(i, b))] if (min(i, b), max(i, b)) in pair_potential else 0
                triangle_potential[(i, j, b)] = pair_potential[(i, j)] * pair_potential[(a, b)] * first_third
            elif j == b and i != a:
                first_second = pair_potential[(min(i, a), max(i, a))] if (min(i, a), max(i, a)) in pair_potential else 0
                triangle_potential[(min(i, a), max(i, a), j)] = pair_potential[(i, j)] * pair_potential[(a, b)] * first_second
    # print(triangle_potential)

    first, second, third = max(triangle_potential, key=triangle_potential.get)
    print(first, second, third)


if __name__ == "__main__":
    main()