## A user-defined stack module
## Change the name of the file to import it (I've named it as such for convenience)

def createstack():
	""" Creates and returns a new stack"""
	return []

def isEmpty(s):
	""" Returns true if the stack is empty else returns false """
	return True if s == [] else False

def peek(s):
	""" Returns the element at the top of the stack. Returns None if the stack is empty"""
	return None if isEmpty(s) else s[-1]

def push(s, elem):
	""" Pushes the element to the top of the stack and returns the new stack"""
	return s + [elem] # append() does not return the list so is not used

def pop(s):
	""" Pops(removes from stack) the top of the stack and returns the element that was popped. Returns None if the stack is empty"""
	return None if isEmpty(s) else s[:-1]
 