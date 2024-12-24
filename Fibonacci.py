# Iterative approach
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Recursive approach
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Test both functions for n = 7
n = 7
print("Iterative result for Fibonacci(7):", fibonacci_iterative(n))
print("Recursive result for Fibonacci(7):", fibonacci_recursive(n))