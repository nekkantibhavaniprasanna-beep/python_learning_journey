# 1. Add
add = lambda a, b: a + b
print("1.", add(10, 20))

# 2. Subtract
sub = lambda a, b: a - b
print("2.", sub(20, 10))

# 3. Multiply
mul = lambda a, b: a * b
print("3.", mul(5, 4))

# 4. Divide
div = lambda a, b: a / b
print("4.", div(20, 5))

# 5. Square
square = lambda x: x * x
print("5.", square(6))

# 6. Cube
cube = lambda x: x ** 3
print("6.", cube(3))

# 7. Even Check
is_even = lambda x: x % 2 == 0
print("7.", is_even(8))

# 8. Odd Check
is_odd = lambda x: x % 2 != 0
print("8.", is_odd(7))

# 9. Maximum
maximum = lambda a, b: a if a > b else b
print("9.", maximum(15, 8))

# 10. Minimum
minimum = lambda a, b: a if a < b else b
print("10.", minimum(15, 8))

# 11. Uppercase
upper = lambda s: s.upper()
print("11.", upper("python"))

# 12. Lowercase
lower = lambda s: s.lower()
print("12.", lower("PYTHON"))

# 13. Length of String
length = lambda s: len(s)
print("13.", length("Python"))

# 14. First Character
first = lambda s: s[0]
print("14.", first("Python"))

# 15. Reverse String
reverse = lambda s: s[::-1]
print("15.", reverse("Python"))

# 16. map() - Square List
numbers = [1, 2, 3, 4, 5]
print("16.", list(map(lambda x: x * x, numbers)))

# 17. map() - Uppercase Names
names = ["alice", "bob", "charlie"]
print("17.", list(map(lambda x: x.upper(), names)))

# 18. filter() - Even Numbers
numbers = [10, 15, 22, 35, 40]
print("18.", list(filter(lambda x: x % 2 == 0, numbers)))

# 19. filter() - Numbers Greater Than 50
numbers = [20, 65, 12, 90, 45, 78]
print("19.", list(filter(lambda x: x > 50, numbers)))

# 20. sorted() - Sort Students by Age
students = [
    ("Alice", 22),
    ("Bob", 19),
    ("Charlie", 25)
]

print("20.", sorted(students, key=lambda x: x[1]))