def alex_win(k, n ,m):
    return False


def main():
    k, n, m = map(int, input().split())
    print("Alex" if alex_win(k, n, m) else "Barb")


if __name__ == "__main__":
    main()