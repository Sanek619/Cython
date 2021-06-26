import time


t_start = time.perf_counter()

cdef long long n = 600000
cdef long long fib1 = 1
cdef long long fib2 = 1
cdef long long i = 0

while i < n - 2:
    current_sum = fib1 + fib2
    fib1 = fib2
    fib2 = current_sum
    i = i + 1

all_time = time.perf_counter() - t_start
print('Time: {:.2f}s'.format(all_time))
