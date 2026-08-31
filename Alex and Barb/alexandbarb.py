def main():
    k, m, n = map(int, input().split())

    if k % (m + n) < m:
        print("Barb")
    else:
        print("Alex")

if __name__ == "__main__":
    main()