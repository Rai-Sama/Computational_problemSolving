from chapt_7_3_8 import *

s = createstack()

if isEmpty(s):
	print("Stack is empty")
else:
	print(s)

print("Pushing elements into the stack:")
for i in range(1, 11):
	s = push(s, i)
	print(s)

if isEmpty(s):
	print("Stack is still empty!")
else:
	print("The stack is no longer empty!")

print(f"The top of the stack now is: {peek(s)}")

print("Popping out the top element of the stack.")
s = pop(s)
print(s)