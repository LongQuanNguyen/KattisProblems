def main():
    items, min_cost = list(map(int, input().split()))
    prices = list(map(int, input().split()))
    prices.sort()
    # print(prices)
    max_items = 1
    for i in range(items-1):
        if prices[i] + prices[i+1] <= min_cost:
            # print(prices[i], prices[i+1])
            max_items = i + 2

    print(max_items)


if __name__ == '__main__':
    main()