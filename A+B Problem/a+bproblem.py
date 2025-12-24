def main():
    num_count = int(input())
    num_list = list(map(int, input().split()))

    occurrence = {}
    for num in num_list:
        if occurrence.get(num) is None:
            occurrence[num] = 1
        else:
            occurrence[num] += 1
    ways = 0
    for i in range(num_count):
        for j in range(i+1,num_count):
            sum = num_list[i] + num_list[j]
            sum_occurrence = occurrence.get(sum)
            # print(i, j, num_list[i], num_list[j], sum, sum_occurrence)
            if sum_occurrence is None:
                continue
            if sum_occurrence == 1 and (sum == num_list[i] or sum == num_list[j]):
                continue
            if sum_occurrence == 2 and sum == num_list[i] and sum == num_list[j]:
                continue
            if sum == num_list[i]:
                sum_occurrence -= 1
            if sum == num_list[j]:
                sum_occurrence -= 1
            ways += 2 * sum_occurrence
    print(ways)

if __name__ == "__main__":
    main()