def fib(int n):
    cdef long fib1 = 1
    cdef long fib2 = 1

    cdef long current_sum = 0

    cdef int i = 0
    while i < n - 2:
        current_sum = fib1 + fib2
        fib1 = fib2
        fib2 = current_sum
        i += 1

    return fib2
