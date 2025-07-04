"""
Problem: Age Calculator

Intuition:
Given a date of birth, calculate the exact **age in years, months, and days** as of today.

Use Python's `datetime` module to:
1. Parse the input birthdate.
2. Get the current date.
3. Calculate differences for year, month, and day.


Time Complexity: O(1)
Space Complexity: O(1)
"""

import datetime
import calendar

def calculate_age(birth_year: int, birth_month: int, birth_date: int)->str:
    today = datetime.date.today()

    """
    Calculate years by directly differencing between current year and birth year
    """
    years = today.year - birth_year

    """
    calculate months by directly differencing between current month ans birth month
    but if month diff < 0 means negative-------------->
        it means we need to move a year back and month will negative+12
    """
    months = today.month - birth_month
    if months < 0:
        months += 12
        years -= 1

    """
    calculate days by finding difference between current date and birth date
    but
    if day diff < 0 means negative----------------?
    it means we need to move one month back and from there we will calculate the day difference
    again here if by moving month a back becomes zero then we will make month =12 and will take previous year month 12 and will get the num of days
    """
    days = today.day - birth_date
    if days<0:
        months-=1
        if months<0:
            months += 12
            years -= 1

        prev_month = today.month - 1 if today.month > 1 else 12
        year_to_considered = today.year if today.month > 1 else today.year-1
        num_of_days = calendar.monthrange(year_to_considered,prev_month)[1]
        days = num_of_days - birth_date + today.day
    return f'{years} YEARS, {months} MONTHS, {days} DAYS'


if __name__ == "__main__":
    print(calculate_age(birth_year=2000,birth_month=12,birth_date=17))