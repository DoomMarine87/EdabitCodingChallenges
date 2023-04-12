"""Write a function that, given a date (in the format MM/DD/YYYY), returns the day of the week as a string. Each day name must be 
one of the following strings: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", or "Saturday".

To illustrate, the day of the week for "12/07/2016" is "Wednesday".
Examples

get_day("12/07/2016") ➞ "Wednesday"

get_day("09/04/2016") ➞ "Sunday"

get_day("12/08/2011") ➞ "Thursday"

Notes

This challenge assumes the week starts on Sunday."""

from datetime import date
def get_day(day):
    return date(int(day[6:]),int(day[0:2]),int(day[3:5])).strftime("%A")

print(get_day("12/07/2016")) # ➞ "Wednesday"
print(get_day("09/04/2016")) # ➞ "Sunday"
print(get_day("12/08/2011")) # ➞ "Thursday"

"""def get_day(day):
	m, d, y = map(int, day.split('/'))
	return date(y, m, d).strftime('%A')"""