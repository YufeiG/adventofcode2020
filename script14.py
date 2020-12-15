#!/usr/bin/env python3
import re

def convert_mask_or(mask_string):
	mask = 0
	for i, c in enumerate(mask_string):
		if c == "1":
			mask += 1
		if len(mask_string) -1 != i:
			mask = mask << 1
	return mask


def convert_mask_and(mask_string):
	mask = 0
	for i, c in enumerate(mask_string):
		if c != "0":
			mask += 1
		if len(mask_string) -1 != i:
			mask = mask << 1
	return mask

def flip(value, i) -> int:
	mask = 1 << i
	return value ^ mask

def generate_all_values(value, x_mask):
	all_values = [value]
	print(x_mask, value)
	for i, c in enumerate(reversed(x_mask)):
		if c == "X":
			new_values = []
			print(i)
			for v in all_values:
				flipped = flip(v, i)
				new_values.append(v)
				new_values.append(flipped)
			all_values = new_values

	return all_values

def process_lines(f):
	mem = {}

	or_mask = 0
	#and_mask = 0
	current_mask_string = None

	for line in f:
		match = re.match("^mask = ([X10]{36})$", line)
		if match:
			current_mask_string = match.group(1)
			or_mask = convert_mask_or(current_mask_string)
			#and_mask = convert_mask_and(current_mask_string)
		else:
			mem_match = re.match("^mem\[([0-9]+)\] = ([0-9]+)$", line)
			assert mem_match
			mem_loc = int(mem_match.group(1))
			mem_value = int(mem_match.group(2))
			mem_loc = mem_loc | or_mask
			print("{}, {}".format(mem_value, or_mask))
			# mem_value = mem_value & and_mask
			all_values = generate_all_values(mem_loc, current_mask_string)
			for v in all_values:
				mem[v] = mem_value
	s = 0
	for loc, value_tuple in mem.items():
		value = value_tuple
		s += value
	print(s)


with open('input14.txt', 'r') as f:
	process_lines(f)
