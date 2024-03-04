def main():
    num_test = int(input())

    for case in range(num_test):
        num_ppl = int(input())
        level_dict = {}

        for person in range(num_ppl):
            name, level, ignore = input().split()
            name = name[:-1]
            level = level.split('-')
            int_lvl = []
            level.reverse()
            # print(name, level)

            # convert level into int
            for i in level:
                if i == 'upper':
                    int_lvl += '3'
                if i == 'middle':
                    int_lvl += '2'
                if i == 'lower':
                    int_lvl += '1'

            if len(level) < 10:
                # Assume middle class fof missing levels
                int_lvl += ['2']*(10 - len(level))
            level_dict[name] = int(''.join(list(map(str, int_lvl))))

            # Sort by name, then level
            level_dict = dict(sorted(level_dict.items(), key=lambda item: (-item[1], item[0])))

        for key in level_dict:
            print(key)
        print(''.join(['=']*30))


if __name__ == '__main__':
    main()
