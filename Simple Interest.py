#Write a program to calculate simple interest
principal = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interest rate (in percentage): "))
time_period = float(input("Enter the time period (in years): "))
interest = (principal * interest_rate * time_period) / 100
print("Simple Interest: ", interest)

'''
Enter the principal amount: 1000
Enter the annual interest rate (in percentage): 5
Enter the time period (in years): 3
Simple Interest: 150.0
'''
