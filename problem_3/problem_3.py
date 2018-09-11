#!/usr/bin/env python

# The prime factors of 13195 are 5, 7, 13, 29
# What is the largest prime factor of the number 600851475143?

from timeit import default_timer as timer

def problem_3(number):

    """
    >>> problem_3(10)
    2**1
    5**1
    5
    >>> problem_3(20)
    2**2
    5**1
    5
    >>> problem_3(125)
    5**3
    5
    >>> problem_3(13195)
    5**1
    7**1
    13**1
    29**1
    29
    """

    # Place to save all primes we encountered less than number
    primes = [ 2 ]
    # Place to save all prime factors of the number
    # and how many times we can use them
    factors_value = [ ]
    factors_power = [ ]

    # First of all lets check if the number is even
    # and how many times we can reduce it to odd one
    if number % primes[-1] == 0:

        factors_value.append(primes[-1])
        factors_power.append(1)

        number /= factors_value[-1]

        while number % factors_value[-1] == 0 and number != 1:
            factors_power[-1] += 1
            number /= factors_value[-1]

        # if the number was a power of 2 we will reach 1 eventually
        # thus we can return
        if number == 1:
            print("{}**{}".format(factors_value[-1], factors_power[-1]))
            return factors_value[-1]
        else:
            print("{}**{}".format(factors_value[-1], factors_power[-1]))

    # Lets go through all odd numbers, starting with 3
    # and less or equal to the number
    i = 2
    while i < int(number) + 1:
        i += 1

        prime_flag = True

        # go over all primes to check if i is a prime
        for k in primes:
            if i%k == 0:
                prime_flag = False
                break

        if prime_flag:
            # if i was a prime append it to the prime list
            primes.append(i)

            # do the same as the first prime
            if number % primes[-1] == 0:

                factors_value.append(primes[-1])
                factors_power.append(1)

                number /= factors_value[-1]

                while number % factors_value[-1] == 0 and number != 1:
                    factors_power[-1] += 1
                    number /= factors_value[-1]

                if number == 1:
                    print("{}**{}".format(factors_value[-1], factors_power[-1]))
                    return factors_value[-1]
                else:
                    print("{}**{}".format(factors_value[-1], factors_power[-1]))

if __name__ == "__main__":

    import doctest
    doctest.testmod()

    #num = int(600851475143)
    num = int(9779)
    t0 = timer()

    print("result = {}".format(problem_3(num)))
    print("time = {} ms".format((timer()-t0)*1e3))
