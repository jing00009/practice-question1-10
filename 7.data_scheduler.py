from datetime import datetime

def date_passed(todays_date, scheduled_date):
    # Define a mapping for month names to month numbers
    month_mapping = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
        'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
    }

    # Function to convert date string to a datetime object
    def parse_date(date_str):
        day, month = date_str.split()
        day = int(day[:-2])  # Remove the 'th', 'st', 'nd', 'rd' from the day
        month = month_mapping[month]
        return datetime(datetime.now().year, month, day)

    # Convert strings to datetime objects
    today = parse_date(todays_date)
    scheduled = parse_date(scheduled_date)

    # Compare the dates and print the result
    if scheduled < today:
        print(f"The scheduled date ({scheduled_date}) has passed.")
    elif scheduled == today:
        print(f"The scheduled date ({scheduled_date}) is today.")
    else:
        print(f"The scheduled date ({scheduled_date}) is yet to pass.")

print(date_passed('26th March', '25th March'))
print(date_passed('26th March', '26th March'))
print(date_passed('26th March', '27th March'))
