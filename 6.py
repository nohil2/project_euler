
"""
Problem 6

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


sum_of_squares = 0
square_of_sum = 0

for x in range(1, 101):
    sum_of_squares += x**2
    square_of_sum += x
    
square_of_sum **= 2

print(square_of_sum - sum_of_squares)