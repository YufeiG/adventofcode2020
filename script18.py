#!/usr/bin/env python3
import re

def multiply_list(myList) :
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x 
    return result 

def rindex(li, v):
	return len(li) - 1 - li[::-1].index(v)

def calculate_no_brackets(values):
	# array
	if len(values) == 0:
		return 0
	operator = None

	multiply_stack = []
	print("value '{}'".format(values))
	for v in values:
		if v == " ":
			assert False

		if re.match("^[0-9]+$", v):
			n = int(v)
			if operator is None:
				assert n != 0
				multiply_stack.append(n)
			elif operator == "+":
				last_n = multiply_stack.pop()
				multiply_stack.append(last_n + n)
			elif operator == "*":
				multiply_stack.append(n)
			else:
				assert False
			operator = None

		elif v in ["+", "*"]:
			operator = v
		else:
			assert False, "saw {}".format(v)
	return multiply_list(multiply_stack)

def calculate(line) -> str:
	if len(line.strip()) == 0:
		return 0
	stack = []

	for i, c in enumerate(line):
		if c == " ":
			continue
		if c == ")":
			last_open = rindex(stack, "(")
			assert last_open >= 0
			inner = calculate_no_brackets(stack[last_open+1:])
			stack = stack[:last_open]
			stack.append(str(inner))
		else: 
			stack.append(c)
	return calculate_no_brackets(stack)
	
with open('input18.txt', 'r') as f:
	s = 0
	for line in f:
		s += calculate(line.strip())
	print(s)

