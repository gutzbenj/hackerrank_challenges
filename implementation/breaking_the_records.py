import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    best = scores[0]
    worst = scores[0]
    best_increase = 0
    worst_decrease = 0

    for score in scores[1:]:
        if score > best:
            best = score
            best_increase += 1
        if score < worst:
            worst = score
            worst_decrease += 1

    print(best_increase, worst_decrease)
    sys.stdout.flush()


if __name__ == '__main__':
    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    breakingRecords(scores)
