def main():
    num_tests = int(input())

    while num_tests > 0:
        inp = input()
        recording = list(map(str, inp.split()))

        noise_in4 = []
        while True:
            gather_in4 = input()
            if gather_in4 == "what does the fox say?":
                break
            else:
                noise_in4.append(str(list(map(str, gather_in4.split()))[-1]))

        print(" ".join([x for x in recording if x not in noise_in4]))

        num_tests -= 1

if __name__ == '__main__':
    main()