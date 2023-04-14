"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
import math


def main():
    num = math.pow(2, 1000)
    num = str("{:.0f}".format(num))
    digits = list(map(str, num))
    digits = [eval(i) for i in digits]
    print(sum(digits))


if __name__ == "__main__":
    main()
