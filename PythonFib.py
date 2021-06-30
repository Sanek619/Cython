from time import perf_counter


n = 46
fib1 = 1
fib2 = 1
i = 0

st = perf_counter()

while i < n - 2:
    sum = fib1 + fib2
    fib1 = fib2
    fib2 = sum
    i += 1

ex_time = perf_counter() - st

print('Time elapsed: ', ex_time)
print('Result for n =', n, 'is', fib2)
