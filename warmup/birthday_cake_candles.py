import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    ar_max = max(ar)
    print(sum([n == ar_max for n in ar]))
    sys.stdout.flush()


if __name__ == '__main__':
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    birthdayCakeCandles(ar)
