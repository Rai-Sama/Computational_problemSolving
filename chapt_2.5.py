yr = int(input("Enter your birth year: "))
# Program to approximate how many seconds have passed since your birth
# my accuracy here is ~99.7% if you know your birth time - eg. 1/01/1900 at 21:30
mnth = int(input("Enter your birth month (not in words): "))
day = int(input("Enter the date of the month of your birth: "))

curr_yr = 2023 # current date is 21st jan, 2023
curr_mnth = 1
curr_dt = 21

res = (((curr_yr - 1) - yr) * 365 + ((12 - mnth) * 30.5) + (curr_mnth - 1) * 30.5 + curr_dt) * 24 * 60 * 60
print(f"It has been approximately {res} seconds since your birth")