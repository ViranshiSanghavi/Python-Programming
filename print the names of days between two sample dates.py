#Write a program that prints the names of days between two sample dates

import datetime

start_date = datetime.date(2023, 1, 1)  # Sample start date (YYYY, MM, DD)
end_date = datetime.date(2023, 1, 10)   # Sample end date (YYYY, MM, DD)

current_date = start_date

while current_date <= end_date:
    print(current_date.strftime("%A"))  # Print the day of the week
    current_date += datetime.timedelta(days=1)

'''
user

import datetime

# Get user input for the start and end dates
start_date_str = input("Enter the start date (YYYY-MM-DD): ")
end_date_str = input("Enter the end date (YYYY-MM-DD): ")

# Convert the input strings to datetime objects
start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()

# Ensure the start date is before the end date
if start_date > end_date:
    print("Start date should be before the end date.")
else:
    current_date = start_date

    while current_date <= end_date:
        print(current_date.strftime("%A"))  # Print the day of the week
        current_date += datetime.timedelta(days=1)

'''
