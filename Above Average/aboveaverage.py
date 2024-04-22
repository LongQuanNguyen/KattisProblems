def main():
    cases = int(input())

    for i in range(cases):
        case = list(map(int, input().split()))
        num_ppl = case[0]
        grades = case[1:]
        average = sum(grades) / num_ppl
        above_aver_count = 0
        for grade in grades:
            if grade > average:
                above_aver_count += 1

        print(format((above_aver_count / num_ppl * 100), '.3f')+'%')


if __name__ == "__main__":
    main()
