# If the year is not divisible by 4, it's a common year.
# If the year is divisible by 4 but not by 100, it's a leap year.
# If the year is divisible by 100 but not by 400, it's a common year.
# If the year is divisible by 400, it's a leap year.

year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")
