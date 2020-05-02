import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum_arr = sum(arr)
    print(sum_arr - max(arr), sum_arr - min(arr))
    sys.stdout.flush()


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
