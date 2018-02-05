# Q04_determine_leap_year.py

# Input
year = int(input("Enter year: "))

# Programming
if year % 400 == 0:
    print("Leap")
elif year % 100 == 0:
    print("Non-Leap")
elif year % 4 == 0:
    print("Leap")
else:
    print("Non-Leap")