def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

n = 15
result = fibonacci(n)
print(f"Fibonacci series with the first {n} numbers: {result}")
