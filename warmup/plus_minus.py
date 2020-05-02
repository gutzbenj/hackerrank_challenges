import sys


def solve():
    size = int(input())

    integers = [int(n) for n in input().split()]

    n_positive, n_negative, n_zero = 0, 0, 0

    for i in integers:
        if i > 0:
            n_positive += 1
        elif i == 0:
            n_zero += 1
        else:
            n_negative += 1

    print(n_positive / size)
    print(n_negative / size)
    print(n_zero / size)
    sys.stdout.flush()


if __name__ == "__main__":
    solve()
