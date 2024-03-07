def bfs_zone(maps, r, c):
    queue = []
    visited = [[False] * c for _ in range(r)]
    zones = [[-1] * c for _ in range(r)]
    zone_id = 0

    for i in range(r):
        for j in range(c):
            if not visited[i][j] and zones[i][j] == -1:
                visited[i][j] = True
                zones[i][j] = zone_id
                queue.append((i, j))

                while len(queue) > 0:
                    x, y = queue.pop(0)
                    for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                        new_x = x + dx
                        new_y = y + dy
                        # lazy evaluation
                        if (0 <= new_x < r and 0 <= new_y < c and
                                not visited[new_x][new_y] and
                                maps[x][y] == maps[new_x][new_y]):
                            visited[new_x][new_y] = True
                            zones[new_x][new_y] = zone_id
                            queue.append((new_x, new_y))
                zone_id += 1
    return zones


def main():
    r, c = map(int, input().split())
    maps = [list(map(int, input())) for _ in range(r)]
    # print(maps)

    n = int(input())
    queries = [list(map(int, input().split())) for _ in range(n)]
    # print(queries)

    zones = bfs_zone(maps, r, c)
    # print(zones)

    for query in queries:
        if maps[query[0] - 1][query[1] - 1] != maps[query[2] - 1][query[3] - 1]:
            print('neither')
        else:
            if zones[query[0] - 1][query[1] - 1] == zones[query[2] - 1][query[3] - 1]:
                print('binary' if maps[query[0] - 1][query[1] - 1] == 0 else 'decimal')
            else:
                print('neither')


if __name__ == "__main__":
    main()
