# 2. D4

## Calculating an approximation of how many breaths you've taken
## and how many heartbeats you have had since your birth using accepted avg rates
## of both (different for different stages in life in the case of breathing)

age = float(input("Enter your age in years: "))
mins_in_yr = 365 * 24 * 60
breaths = (45 * mins_in_yr if age >= 1 else 45 * age * mins_in_yr) + (25 * 3 * mins_in_yr if age >= 3 else (25 * (age - 1) * mins_in_yr if age >= 1 else 0)) + (20 * 9 * mins_in_yr if age >= 14 else (20 * (age - 4) * mins_in_yr if age >= 1 else 0)) + (16 * (age-14) * mins_in_yr if age >= 15 else 0)
print(f"You have breathed approximately {format(breaths, ',.2f')} times since your birth")
heart_bts = 67.5 * age * mins_in_yr * 60
print(f"You have had approximately {format(heart_bts, ',.2f')} heartbeats since your birth")