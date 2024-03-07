def main():
    num_ppl, links, days = list(map(int, input().split()))
    skept_dict = {}
    heard_dict = {}
    told_dict = {}
    connections = {}

    for person in range(num_ppl):
        name, skept_lvl = input().split()
        skept_dict[name] = int(skept_lvl)
        heard_dict[name] = False
        told_dict[name] = set()
        connections[name] = []

    for link in range(links):
        p1, p2 = input().split()
        connections[p1].append(p2)
        connections[p2].append(p1)

    origin_p = input()

    spread_q = [(origin_p, 0)]
    while len(spread_q) > 0:
        current_p, current_day = spread_q.pop(0)

        if current_day < days:
            for person in connections[current_p]:
                heard_dict[person] = True
                told_dict[person].add(current_p)
                if len(told_dict[person]) == skept_dict[person]:
                    spread_q.append((person, current_day + 1))

    heard = 0
    for person in heard_dict:
        if heard_dict[person] and person != origin_p:
            heard += 1

    print(heard)


if __name__ == '__main__':
    main()