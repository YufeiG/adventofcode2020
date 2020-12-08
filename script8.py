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

	while True:
		if i == len(lines):
			print("terminate {}".format(acc))
			return True
		if i > len(lines):
			assert False

		if i in visited_lines:
			#print("looped {}".format(acc))
			return False
		visited_lines.add(i)
		line = lines[i]
		if line.strip() == "":
			print("Complete")
			return False
		(r, a) = process_line(line, change_index == i)
		acc += a
		i += r

with open('input8.txt', 'r') as f:
	lines = f.read().split("\n")[:-1]
	s = [0, 1, 2, 3, 4, 513, 514, 515, 518, 519, 520, 7, 8, 9, 10, 11, 16, 17, 18, 19, 533, 534, 27, 28, 29, 30, 539, 540, 541, 34, 548, 549, 550, 39, 40, 41, 551, 556, 44, 45, 46, 47, 50, 51, 564, 565, 566, 568, 569, 59, 62, 575, 576, 577, 578, 579, 66, 67, 71, 72, 73, 74, 592, 593, 83, 84, 85, 597, 87, 88, 89, 90, 91, 598, 605, 606, 607, 608, 609, 601, 611, 100, 101, 102, 103, 620, 621, 622, 128, 129, 130, 131, 132, 138, 139, 140, 141, 147, 148, 149, 150, 151, 154, 155, 156, 161, 184, 185, 186, 196, 199, 200, 201, 202, 203, 209, 222, 223, 224, 225, 231, 234, 235, 236, 239, 240, 241, 242, 250, 251, 255, 256, 257, 265, 266, 267, 268, 272, 277, 278, 305, 306, 307, 308, 309, 312, 313, 314, 315, 320, 321, 322, 323, 324, 330, 331, 337, 362, 363, 364, 366, 367, 374, 375, 376, 377, 382, 394, 395, 396, 398, 399, 400, 405, 406, 420, 421, 422, 427, 428, 429, 430, 432, 433, 434, 439, 440, 441, 442, 443, 447, 448, 449, 450, 599, 455, 456, 457, 458, 459, 600, 464, 465, 466, 467, 468, 505, 506, 507]
	for k in s:
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

