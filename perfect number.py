def is_perfect(n):
    # Sum all numbers that divide n perfectly (excluding n itself)
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    
    # Check if the sum equals the original number
    return divisor_sum == n

# Test the function
print(is_perfect(6))   # True (1 + 2 + 3 = 6)
print(is_perfect(28))  # True (1 + 2 + 4 + 7 + 14 = 28)
print(is_perfect(10))  # False
