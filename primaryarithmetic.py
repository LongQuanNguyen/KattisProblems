def main():
    while True:
        inp = input()
        if inp == '0 0':
            break

        first, second = list(inp.split())
        first = list(map(int, list(first)))
        first.reverse()
        second = list(map(int, list(second)))
        second.reverse()

        if len(first) > len(second):
            for i in range(len(first) - len(second)):
                second.append(0)

        if len(first) < len(second):
            for i in range(len(second) - len(first)):
                first.append(0)

        #print(first, second)

        total_carry = 0
        pre_carry = 0
        for i in range(len(first)):
            if first[i] + second[i] + pre_carry >= 10:
                pre_carry = 1
                total_carry += 1
            else:
                pre_carry = 0

        if total_carry == 0:
            print('No carry operation.')
        elif total_carry == 1:
            print('1 carry operation.')
        else:
            print(total_carry, 'carry operations.')

if __name__ == '__main__':
    main()