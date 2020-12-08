#!/usr/bin/env python3
import re
# jmp->nop OR nop->jmp
def process_line(line, swap = False) -> (int, int):
	match = re.match("^(acc|jmp|nop) (\+|-)([0-9]+)$", line.strip())

	action = match.group(1)
	sign = match.group(2)
	value = int(match.group(3))
	#print("{} / {} / {}".format(action, sign, value))
	if sign == "-":
		value = value * (-1)

	if action == "acc":
		return (1, value)
	elif action == "nop":
		if swap:
			return (value, 0)
		return (1, 0)
	elif action == "jmp":
		if swap:
			return (1, 0)
		return (value, 0)
	else:
		assert False

def does_terminate(lines, change_index) -> bool:
	i = 0
	acc = 0
	visited_lines = set()

	while i < len(lines):
		if i in visited_lines:
			return False
		visited_lines.add(i)
		line = lines[i]
		(r, a) = process_line(line, change_index == i)
		acc += a
		i += r
	print("terminate {}".format(acc))
	return True

with open('input8.txt', 'r') as f:
	lines = f.read().split("\n")[:-1]
	for k in range(len(lines)):
		if does_terminate(lines, k):
			exit()

def blah(lines):
	i = 0
	visited_lines = set()
	acc = 0
	while True:
		if i >= len(lines):
			print("Error")
			exit()
		if i in visited_lines:
			print(acc)
			print(visited_lines)
			exit()
		visited_lines.add(i)
		line = lines[i]
		(r, a) = process_line(line)
		acc += a
		i += r

		# acc = 1723

