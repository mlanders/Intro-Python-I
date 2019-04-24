"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

today = datetime.today()
calendar.setfirstweekday(calendar.SUNDAY)
c = calendar.TextCalendar()


def cal(year, month):
    if len(month) == 0 or len(year) == 0:
        if len(month) == 0 and len(year) > 0:
            year = int(year)
            if year > today.year:
                print("please enter a valid year")
            else:
                month = today.month
                print(c.formatmonth(year, month))

        if len(month) > 0 and len(year) == 0:
            month = int(month)
            if month < 1 or month > 12:
                print("please enter a valid month")
            else:
                year = today.year
                print(c.formatmonth(year, month))

        if len(month) == 0 and len(year) == 0:
            year = today.year
            month = today.month
            print(c.formatmonth(year, month))
    else:
        month = int(month)
        year = int(year)
        if month < 1 or month > 12:
            print("please enter a valid month")
        elif year > today.year:
            print("Invalid year")
        else:
            print(c.formatmonth(year, month))


x = input("Enter in the year:")
y = input("Enter in the month:")

cal(x, y)
