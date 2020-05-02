import sys

# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
def getTotalX(a, b):
    # Write your code here
    numbers_between = 0

    for i in range(a[-1], b[0]+1):
        if all([i % num == 0 for num in a]) and all([num % i == 0 for num in b]):
            numbers_between += 1

    print(numbers_between)
    sys.stdout.flush()


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    getTotalX(arr, brr)
