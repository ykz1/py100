from datetime import date

today = date.today()

today_year = today.year             # The .year method specifically returns just the year of a date.
iso_year = today.isocalendar()[0]   # The .isocalendar() method returns year, month, and day of month. Calling the first element [0] retrieves only the year.

print(today_year)
print(iso_year)

# Question: why does .year not need brackets i.e. ".year()", but .isocalendar() does? How would we know this syntax difference if we haven't used these methods before?