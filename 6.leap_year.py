def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if it's a century year (ending in 00)
        if year % 100 == 0:
            # Check if it's also divisible by 400 to be a leap year
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(is_leap_year(1990))
print(is_leap_year(2023))
print(is_leap_year(1993))
print(is_leap_year(2000))
