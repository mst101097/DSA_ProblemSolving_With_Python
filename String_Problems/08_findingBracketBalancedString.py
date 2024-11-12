'''
Check for Balanced Brackets in an expression (well-formedness) using Stack
Given an expression string exp, write a program to examine
whether the pairs and the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in exp.

Input: exp = “[()]{}{[()()]()}”
Output: Balanced

Input: exp = “[(])”
Output: Not Balanced

'''
def findBracketBalance(str1):

	stack = []

	for char in str1:

		if char in ['[','{','(']:
			stack.append(char)

		else:
			if not stack:
				return False

			currentChar = stack.pop()

			if currentChar =='[':
				if char != ']':
					return False

			if currentChar =='{':
				if char != '}':
					return False

			if currentChar =='(':
				if char != ')':
					return False
	if stack:
		return False
	return True

# inputStr = "{()[]"
inputStr = "[()]{}{[()()]()}"

if findBracketBalance(inputStr):
	print('Balanced String ')
else:
	print('Not Balanced')


