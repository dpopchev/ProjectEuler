#!/usr/bin/env python

# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# The sum of all multiples of k less than N:
#   k1 + k2 + k3 + k4 + k5 +...+ n = k*(1 + 2 + 3 + 4 + 5 +...+ p) =
#   = k*(1/2)*p*(p+1), where p = n/k
# With n we label the greatest multiple of k less than N, which we should find
#
# We presume the list of multiples is restricted to prime numbers
# without repetition
#
# We need to take into account that the SumDivisibleBy(3) + SumDivisibleBy(5)
# Is including of SumDivisibleBy(15) twice, thus we need to subtract them out
#
# It will be similar for arbitrary list of multiples, so we should create a
# list of all possible combinations of k[] to subtract from the final sum

# returns the greatest number divisible by k and less or equal to N
def FindGreatestNumDivisibleBy(k, N):

    """
    >>> FindGreatestNumDivisibleBy(2, 10)
    10
    >>> FindGreatestNumDivisibleBy(3, 19)
    18
    >>> FindGreatestNumDivisibleBy(5, 23)
    20
    """

    while N%k != 0:
        N -= 1

    return int(N)

# returns the sum of all numbers less or equal to target and divisible by k
def SumOfMultiple(k, target):

    """
    >>> SumOfMultiple(1,3)
    6
    >>> SumOfMultiple(5,10)
    15
    >>> SumOfMultiple(2,6)
    12
    """

    p = FindGreatestNumDivisibleBy(k, target)/k

    return int(k*(1/2)*p*(p+1))

# finds all possible products of the numbers provided in k_list
# and return extended one with all possible multiples
def FindCombinedMultiple(k_list):

    """
    >>> FindCombinedMultiple([2,3])
    [6]
    >>> FindCombinedMultiple([3,5])
    [15]
    >>> FindCombinedMultiple([3,5,7])
    [15, 21, 35]
    """

    from itertools import combinations

    multiple_list = []

    for single_combination in combinations(k_list,2):
        multiple_list.append(single_combination[0]*single_combination[1])

    return multiple_list

# Function to return sum of all numbers, who are multiples of the numbers in
# list k, and less than the number target
def FindSumOfMultiples(k, target):

    """
    >>> FindSumOfMultiples([3,5], 10)
    23
    """

    k_combined = FindCombinedMultiple(k)
    target -= 1

    result = 0
    for i in k:
        result += SumOfMultiple(i,target)

    for i in k_combined:
        result -= SumOfMultiple(i,target)

    return int(result)

if __name__ == '__main__':

    import doctest

    from timeit import default_timer as timer

    doctest.testmod()

    multiples_list = [3,5]
    #target = 10;
    target = 1000;

    t0 = timer();
    print("result = {}".format(FindSumOfMultiples(multiples_list,target)))

    print("time = {} ms".format((timer()-t0)*1e3))
