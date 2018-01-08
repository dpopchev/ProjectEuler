#!/usr/bin/env python

# Each new term in the Fibonacci sequence is generated by adding the
# previous two terms.
# By starting with 1 and 2, the first 12 terms will be:
#   1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,...
#
# By considering the terms in the Fibonacci sequence whose
# values do not exceed four million, find the sum of the even-valued terms.

def problem_2(max_number):

    """
    >>> problem_2(10)
    10
    >>> problem_2(20)
    10
    >>> problem_2(35)
    44
    """

    sum_even_num = 0
    fib_num_1 = 1
    fib_num_2 = 1

    # have we reached the maximum Fibonacci number value
    while fib_num_2 < max_number:

        # add to the overall sum if it is even
        sum_even_num += fib_num_2 if fib_num_2 % 2 == 0 else 0

        # the last Fibonacci number fib_num_2 becomes previous fib_num_1
        #
        # the new Fibonacci number is the sum of the previous two
        # thus save in fib_num_2 = fib_num_1 + fib_num_2
        fib_num_1, fib_num_2 = fib_num_2, fib_num_1 + fib_num_2
        #print(fib_num_1, fib_num_2)

    return sum_even_num

if __name__ == "__main__":

    import doctest

    from timeit import default_timer as timer

    doctest.testmod()

    maximum_fibonaci_value = 4e6
    #maximum_fibonaci_value = 10

    t0 = timer();
    print("result = {}".format(problem_2(maximum_fibonaci_value)))

    print("time = {} ms".format((timer()-t0)*1e3))






