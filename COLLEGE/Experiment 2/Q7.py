"""7.	Write a program which takes any date as input and display next date of the calendar
e.g.
I/P: day=20 month=9 year=2005 
O/P: day=21 month=9 year 2005
"""
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
# Days in each month
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if day < 30: # Simplified: assuming all months have 30 days
    day += 1
else:
    day = 1
    if month < 12:
        month += 1
    else:
        month = 1
        year += 1

print("Next Date:", day, "/", month, "/", year)
