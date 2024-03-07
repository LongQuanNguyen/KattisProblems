def check(n):
    ops = ['*', '+', '-', '//']
    if n > 256 or n < -60:
        return 'no solution'
    for first_op in ops:
        for second_op in ops:
            for third_op in ops:
                eq = '4 ' + first_op + ' 4 ' + second_op + ' 4 ' + third_op + ' 4'
                if eval(eq) == n:
                    return (eq + ' = ' + str(n)).replace('//', '/')
    return 'no solution'


def main():
    num_tests = int(input())
    for i in range(num_tests):
        n = int(input())
        print(check(n))


if __name__ == "__main__":
    main()