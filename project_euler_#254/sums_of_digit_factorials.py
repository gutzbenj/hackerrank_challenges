import sys


def factorial(n):
    if n == 0:
        return 1

    total = 1
    for i in range(1, n+1):
        total *= i

    return total


factorials_ = {
    n: factorial(n)
    for n in range(10)
}


def f(n):
    total = 0
    for num in str(n):
        total += factorials_[int(num)]

    return total


def sf(n):
    total = 0
    for i in str(f(n)):
        total += int(i)

    return total


def g(i):
    n = 0
    while True:
        n += 1

        if sf(n) == i:
            return n


def sg(i):
    total = 0
    for num in str(g(i)):
        total += int(num)
    return total


def solve_single(n, m):
    total = 0
    for i in range(1, n+1):
        total += sg(i)

    return total % m


def solve():
    q = int(input())

    for i in range(q):
        n, m = input().split()
        print(solve_single(int(n), int(m)))
        sys.stdout.flush()


if __name__ == "__main__":
    # solve()
    print(solve_single(40, 1000000))
