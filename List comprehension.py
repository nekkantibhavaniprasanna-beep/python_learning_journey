# 1. Squares
[x**2 for x in range(1, 6)]

# 2. Cubes
[x**3 for x in range(1, 6)]

# 3. Even numbers
[x for x in range(1, 11) if x % 2 == 0]

# 4. Odd numbers
[x for x in range(1, 11) if x % 2 != 0]

# 5. Even squares
[x**2 for x in range(1, 11) if x % 2 == 0]

# 6. Uppercase words
[word.upper() for word in ["apple", "banana", "mango"]]

# 7. String lengths
[len(word) for word in ["apple", "banana", "mango"]]

# 8. First letter of each word
[word[0] for word in ["apple", "banana", "mango"]]

# 9. Characters of a string
[ch for ch in "Python"]

# 10. Digits from 0 to 9 as strings
[str(x) for x in range(10)]

# 11. Multiples of 5
[x for x in range(1, 51) if x % 5 == 0]

# 12. Negative numbers
[-x for x in range(1, 6)]

# 13. Boolean values (even?)
[x % 2 == 0 for x in range(1, 6)]

# 14. Replace even with "Even", odd with "Odd"
["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]

# 15. Flatten a 2D list
[num for row in [[1, 2], [3, 4], [5, 6]] for num in row]

# 16. Cartesian product
[(x, y) for x in [1, 2, 3] for y in ['A', 'B']]

# 17. Vowels from a string
[ch for ch in "Artificial Intelligence" if ch.lower() in "aeiou"]

# 18. Remove spaces
[ch for ch in "Hello World" if ch != " "]

# 19. Numbers divisible by both 2 and 3
[x for x in range(1, 31) if x % 2 == 0 and x % 3 == 0]

# 20. Squares greater than 50
[x**2 for x in range(1, 11) if x**2 > 50]