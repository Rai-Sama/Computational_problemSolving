# Problem given in Chapter 1 - 1.7 --- Drake equation
r = 7
p = float(input("p: "))
n = float(input("n: "))
f = float(input("f: "))
i = float(input("i: "))
c = float(input("c: "))
l = float(input("L: "))

res = r * p * n * f * i * c * l
print(f"Based on your assumptions there are {res} possible intelligent civilizations in the galaxy")