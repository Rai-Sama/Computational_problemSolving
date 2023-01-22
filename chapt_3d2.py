# 3. D2

## Displaying all the leap years b/w the current year and any future year given by the user

import datetime
curr_yr = datetime.date.today().year
end_yr = int(input("Enter the year you want to end the calculation at: "))

print(f"The following are the leap years between the current year and {end_yr} : ")
while curr_yr <= end_yr:
	if curr_yr % 4 == 0:
		if curr_yr % 100 == 0:
			if curr_yr % 400 == 0:
				print(f"{curr_yr}")
				curr_yr += 1
			else:
				curr_yr += 1
				continue
		else:
			print(f"{curr_yr}")
			curr_yr += 1
	else:
		curr_yr += 1
