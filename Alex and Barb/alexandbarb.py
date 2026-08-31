def alex_win(card_left, min_draw , max_draw, cache):
    if card_left in cache:
        return cache[card_left]

    if card_left < min_draw:
        cache[card_left] = False
        return False

    for draw in range(min_draw, min(max_draw, card_left) + 1):
        if not alex_win(card_left - draw, min_draw, max_draw, cache):
            cache[card_left] = True
            return True

    cache[card_left] = False
    return False

def main():
    k, m, n = map(int, input().split())
    cache = {}
    print("Alex" if alex_win(k, m, n, cache) else "Barb")

if __name__ == "__main__":
    main()