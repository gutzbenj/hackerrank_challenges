import sys

# Complete the timeConversion function below.
def timeConversion(s):
    _am_or_pm = s[-2:]

    regular_time = s[:-2]
    hour = regular_time[:2]

    if _am_or_pm == "PM" and hour != "12":
        regular_time = str(int(hour) + 12) + regular_time[2:]
    elif _am_or_pm == "AM" and hour == "12":
        regular_time = "00" + regular_time[2:]

    print(regular_time)
    sys.stdout.flush()


if __name__ == '__main__':
    s = input().strip()

    timeConversion(s)
