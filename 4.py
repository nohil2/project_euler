"""
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

num_list = []
l_p = 0

for x in range(100, 1000):
    for y in range(100, 1000):
        p = x * y
        if str(p) == str(p)[::-1]:
            if p > l_p:
                l_p = p

print(l_p)