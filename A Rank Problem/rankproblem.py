def main():
    teams, games = list(map(int, input().split()))
    rank_list = ["T"+str(i) for i in range(1, teams + 1)]

    for _ in range(games):
        w, l = input().split()
        if rank_list.index(w) > rank_list.index(l):
            rank_list.insert(rank_list.index(w) + 1, l)
            rank_list.remove(l)

    print(' '.join(rank_list))


if __name__ == '__main__':
    main()