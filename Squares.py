#Write a program to output the squares (using multiplication) of numbers from 1 to 5 on separate lines.
n = int(input())
for i in range(1,n):
    print(f"{i}-{i**2}")
