from time import perf_counter

from fib import fib

st = perf_counter()
n = 46
ans = fib(n)
ex_time = perf_counter() - st

print('Time elapsed:', ex_time)
print('Result for n =', n, 'is', ans)
