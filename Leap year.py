def is_leap_year(year):
    # Divisible by 4 and not 100, OR divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Get input from the user
user_input = int(input("Enter a year: "))

if is_leap_year(user_input):
    print(f"{user_input} is a leap year.")
else:
    print(f"{user_input} is not a leap year.")
