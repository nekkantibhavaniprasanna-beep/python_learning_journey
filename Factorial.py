
def factorial_loop(n):
    if n < 0:
        return "Undefined for negative numbers"
    
    result = 1
    for i in range(1, n + 1):
        result *= i  # Multiplies result by each number up to n
    return result

# Example usage:
print(factorial_loop(5))  # Output: 120
print(factorial_loop(0))  # Output: 1