#!/usr/bin/env python

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit
# numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

from timeit import default_timer as timer

primes = [ 2 ]

# Procedure to factorize the given number to powers of prime numbers
# it will keep all prime numbers it encounter in global list
# it will return list of the factors of the number
def factorize(num):

    factor_value = []
    factor_power = []

    for i in primes:

        if num % i == 0:

            factor_value.append(i)
            factor_power.append(1)

            num /= factor_value[-1]

            while num % factor_value[-1] == 0 and num != 1:
                factor_power[-1] += 1
                num /= factor_value[-1]

    if num == 1:
        return [ factor_value, factor_power ]
    else:
        i = primes[-1]

        while i < int(num) + 1:

            i += 1

            prime_flag = True

            for k in primes:
                if i%k == 0:
                    prime_flag = False
                    break

            if prime_flag:
                primes.append(i)

                if num % primes[-1] == 0:

                    factor_value.append(primes[-1])
                    factor_power.append(1)

                    num /= factor_value[-1]

                    while num % factor_value[-1] == 0 and num != 1:
                        factor_power[-1] += 1
                        num /= factor_value[-1]

                    if num == 1:
                        return [ factor_value, factor_power ]

# Procedure to check if a given number is palindrome or not
# returns True if it is
# returns False if it is not
# It achieves the goal by reversing num and checking if they are equal
def palindrome_check(num):

    n = num
    rev = 0

    while n > 0:

        dig = int(n % 10)
        rev = rev*10 + dig
        n = int(n / 10)

    if(rev == num):
        return True
    else:
        return False

# We provide how many digits each of the numbers, whos product should be
# a palindrome should have
# We calculate the largest possible product and start reducing it by 1
# We check the number if it is a palindrome
# if it is, we factorize it by keeping track of the prime numbers we encounter
# when we have factorized the number we create half of all possible combinations
# we can create from the factor list and calculate one of the products
# if the product is equal to the desired amount of digits we check if
# it is a factor of the palindrome and if the result is also equal to the
# desired amount of digits - if so this is our result
def problem_4(num_digits):

    """
    >>> problem_4(2)
    [9009, 99, 91]
    """

    from math import pow
    from itertools import combinations

    max_number = pow(( pow(10,num_digits)-1 ), 2)

    for single_number in range(int(max_number), 10, -1):

        # check if single_number is palindrome
        if palindrome_check(single_number):

            # factorize the number to prime factors in res[0]
            # and their powers containing in res[1]
            res = factorize(single_number)

            # list containing the factors of the single_number
            factors = [ m**n for m,n in zip(res[0], res[1]) ]

            # start creating half of all possible combinations of the factors
            for combination_class in \
              range( \
                len(factors) - 1, \
                int(len(factors)/2)-1 \
                    if (len(factors)/2)%2 == 0 else int(len(factors)/2), \
               -1 \
            ):
                for combination_single in combinations(factors,combination_class):

                    # of this particular combination create the product
                    product_1= 1
                    for _i in combination_single:
                        product_1 *= _i

                    # if the product is with the desired number of digits
                    # calculate the other product and its reminder
                    if len(str(abs(product_1))) == num_digits:
                        product_2_reminder = single_number % product_1
                        product_2 = int(single_number / product_1)

                        #print(\
                          #single_number, \
                          #res, \
                          #combination_single, \
                          #rest, \
                          #product_1, \
                          #product_2 \
                        #)

                        # if the second product has divides with no reminder
                        # and has the desired number of digits
                        # we have our answer
                        if product_2_reminder == 0 and len(str(abs(product_2))) == num_digits:
                            return [ single_number, product_1, product_2]
    return 0

if __name__ == "__main__":

    import doctest
    doctest.testmod()

    num = 3
    t0 = timer()

    print("result = {}".format(problem_4(num)))
    print("time = {} ms".format((timer()-t0)*1e3))
