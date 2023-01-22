# 3. D4

## Home loan amortization -- calculating monthly payment table for each possible interest rate value
## interest rate can be in the range of 3%-18% (integer values)

amt = float(input("Enter your loan amount: "))
r = [i/100 for i in range(3, 19)]
term = float(input("Enter the term (number of yrs for payment): "))
n = term * 12
d = [((1 + k/12)**n - 1)/((k/12)*(1 + k/12)**n) for k in r]
print(f"Loan amount: {amt}\t Term: {term}")
print("Interest Rate\tMonthly Payment")
for i in range(len(r)):
	print(f"{int(r[i]*100)}%\t{format(amt/d[i],',.2f')}")