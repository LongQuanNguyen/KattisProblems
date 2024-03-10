def main():
    statues = int(input())

    if statues == 0 or statues == 1:
        print(statues)
    else:
        for i in range(20):
            if 2**i < statues <= 2**(i+1):
                print(i+2)


if __name__ == '__main__':
    main()
