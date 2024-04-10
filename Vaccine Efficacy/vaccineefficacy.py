def main():
    num_ppl = int(input())
    vac_count = 0
    a_vac_inf = 0
    b_vac_inf = 0
    c_vac_inf = 0
    non_vac_count = 0
    a_non_vac_inf = 0
    b_non_vac_inf = 0
    c_non_vac_inf = 0
    for person in range(0, num_ppl):
        inp = input()
        if inp[0] == 'Y':
            vac_count += 1
            a_vac_inf += 1 if inp[1] == 'Y' else 0
            b_vac_inf += 1 if inp[2] == 'Y' else 0
            c_vac_inf += 1 if inp[3] == 'Y' else 0
        else:
            non_vac_count += 1
            a_non_vac_inf += 1 if inp[1] == 'Y' else 0
            b_non_vac_inf += 1 if inp[2] == 'Y' else 0
            c_non_vac_inf += 1 if inp[3] == 'Y' else 0

    print('Not Effective' if (a_vac_inf/vac_count >= a_non_vac_inf/non_vac_count)
          else (a_non_vac_inf/non_vac_count - a_vac_inf/vac_count) / (a_non_vac_inf/non_vac_count) * 100)
    print('Not Effective' if (b_vac_inf / vac_count >= b_non_vac_inf / non_vac_count)
          else (b_non_vac_inf/non_vac_count - b_vac_inf/vac_count) / (b_non_vac_inf/non_vac_count) * 100)
    print('Not Effective' if (c_vac_inf / vac_count >= c_non_vac_inf / non_vac_count)
          else (c_non_vac_inf/non_vac_count - c_vac_inf/vac_count) / (c_non_vac_inf/non_vac_count) * 100)


if __name__ == '__main__':
    main()