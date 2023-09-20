def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = 10
result = fibonacci_recursive(n)


def fibonacci_dynamic(n):
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

n = 10
result = fibonacci_dynamic(n)
print(f"Fibonacci({n}) using dynamic programming:", result)
result = fibonacci_recursive(n)
print(f"Fibonacci({n}) using recursive programming:", result)
