#!/usr/bin/env python

# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

from timeit import default_timer as timer

def problem_1( end ):

    """
    >>> problem_1(10)
    23
    >>> problem_1(20)
    78
    """

    # Fill the multiples of 3
    multp3 = [x for x in range(3, end, 3)]

    # Fill the multiples of 5 if they are not present in multp3
    # Example of one occurring in both is 15
    multp5 = [x if x not in multp3 else 0 for x in range(5, end, 5)]

    #print(multp3)
    #print(multp5)

    return sum(multp3) + sum(multp5)

if __name__ == '__main__':

    import doctest
    doctest.testmod()

    target = 1000;
    t0 = timer();
    print("result = {}".format(problem_1(target)))

    print("time = {} ms".format((timer()-t0)*1e3))

