#!/usr/bin/env python3
"""
OPS445 Assignment 1 - Version C - Date Calculator

This program calculates the number of weekend days between two dates.
It automatically determines which date is earlier and uses it as the start date.

Author: Sanjib Shrestha
Student ID: sshrestha183
Date: 2026/07/03

Academic Honesty Declaration: I declare that this is my own original work.
"""

import sys


def leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def mon_max(month, year):
    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if month == 2 and leap_year(year):
        return 29
    return month_days[month]


def after(date):
    day, month, year = (int(x) for x in date.split('/'))
    day += 1
    if day > mon_max(month, year):
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return f"{day:02d}/{month:02d}/{year:04d}"


def before(date):
    day, month, year = (int(x) for x in date.split('/'))
    day -= 1
    if day < 1:
        month -= 1
        if month < 1:
            month = 12
            year -= 1
        day = mon_max(month, year)
    return f"{day:02d}/{month:02d}/{year:04d}"


def valid_date(date):
    try:
        parts = date.split('/')
        if len(parts) != 3:
            return False
        day, month, year = (int(x) for x in parts)
        if month < 1 or month > 12:
            return False
        if day < 1 or day > mon_max(month, year):
            return False
        if year < 1:
            return False
        return True
    except:
        return False


def day_of_week(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    h = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
    days = ['sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri']
    return days[h]


def day_count(start_date, end_date):
    count = 0
    current = start_date
    while True:
        day, month, year = (int(x) for x in current.split('/'))
        if day_of_week(day, month, year) in ['sat', 'sun']:
            count += 1
        if current == end_date:
            break
        current = after(current)
    return count


def usage():
    print("Usage: assignment1.py DD/MM/YYYY DD/MM/YYYY")
    sys.exit(1)


def main():
    if len(sys.argv) != 3:
        usage()
    
    date1 = sys.argv[1]
    date2 = sys.argv[2]
    
    if not valid_date(date1) or not valid_date(date2):
        usage()
    
    # Compare dates correctly
    d1_day, d1_month, d1_year = (int(x) for x in date1.split('/'))
    d2_day, d2_month, d2_year = (int(x) for x in date2.split('/'))
    
    # Convert to comparable numbers
    date1_num = d1_year * 10000 + d1_month * 100 + d1_day
    date2_num = d2_year * 10000 + d2_month * 100 + d2_day
    
    if date1_num <= date2_num:
        start, end = date1, date2
    else:
        start, end = date2, date1
    
    weekends = day_count(start, end)
    print(f"The period between {start} and {end} includes {weekends} weekend days")


if __name__ == "__main__":
    main()
