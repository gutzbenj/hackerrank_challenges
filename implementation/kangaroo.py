import sys


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    can_meet = None
    dist = abs(x1 - x2)
    while True:
        x1 += v1
        x2 += v2

        if abs(x1 - x2) >= dist:
            can_meet = "NO"
            break
        else:
            dist = abs(x1 - x2)

            if dist == 0:
                can_meet = "YES"
                break

    print(can_meet)
    sys.stdout.flush()


if __name__ == '__main__':
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    kangaroo(x1, v1, x2, v2)
