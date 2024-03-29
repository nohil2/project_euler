"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""


def main():
    max_chain = 0
    starting_num = 0
    for i in range(1, 1000000):
        new_chain = collatz(0, i)
        if max_chain < new_chain:
            max_chain = new_chain
            starting_num = i
    print(starting_num, max_chain)


def collatz(chain, n):
    chain = chain + 1
    if n == 1:
        return chain
    elif n % 2 == 0:
        n = n / 2
    else:
        n = n * 3 + 1
    return collatz(chain, n)


if __name__ == "__main__":
    main()
