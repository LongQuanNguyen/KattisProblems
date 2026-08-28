def create_friendship_matrix(n, m):
    adj_matrix = [[0] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int,input().split())
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1
    return adj_matrix


def count_independent_sets(adjacency, n):
    counts = [0] * (n + 1)

    def search(available, group_size):
        if len(available) == 0:
            counts[group_size] += 1
            return

        candidate = available[0]

        # Case 1: Exclude candidate
        search(available[1:], group_size)

        # Case 2: Include candidate
        next_available = []

        for person in available[1:]:
            if adjacency[candidate][person] == 0:
                next_available.append(person)

        search(next_available, group_size + 1)

    search(list(range(1, n + 1)), 0)

    return counts


def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    n, m = map(int,input().split())
    fs_adj_matrix = create_friendship_matrix(n, m)
    # print_matrix(fs_adj_matrix)
    print(" ".join(str(num) for num in count_independent_sets(fs_adj_matrix, n)))


if __name__ == "__main__":
    main()

