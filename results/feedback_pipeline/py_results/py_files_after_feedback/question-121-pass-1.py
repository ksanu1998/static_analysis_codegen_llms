def is_leap_year(year):
    return year % 4 == 0 and (year % 100!= 0 or year % 400 == 0)

def count_leap_years(start, end):
    return sum(1 for year in range(start, end+1) if is_leap_year(year))
