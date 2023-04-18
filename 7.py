import itertools


def prime_gen():
    # Sieve of Eratosthenes
    # Code by David Eppstein, UC Irvine, 28 Feb 2002
    primes = {}
    i = 2
    while True:
        if i not in primes:
            yield i
            primes[i * i] = [i]
        else:
            for j in primes[i]:
                primes.setdefault(j + i, []).append(j)
            del primes[i]
        i += 1


def main():
    gen = prime_gen()
    num = list(itertools.islice(gen, 10001))[-1]

    print(num)


if __name__ == "__main__":
    main()
