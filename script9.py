#!/usr/bin/env python3
import re

def find_sum(sum_value, numbs) -> (int, int):
	# return indices in numbs
	for i in range(len(numbs)):
		for j in range(1, len(numbs)):
			if numbs[i] + numbs[j] == sum_value:
				return (i, j)
	return None

def find_set(sum_value, numbs) -> (int, int):
	# returns start and end indices
	for i in range(len(numbs)):
		for j in range(i+1, len(numbs)):
			current_sum = sum(numbs[i:j+1])
			if sum_value == current_sum:
				return (i, j)
			elif sum_value < current_sum:
				break
	return None

preamble_count = 25
with open('input9.txt', 'r') as f:
	i = 0
	preamble = []
	all_numbs = []
	for line in f:
		number = int(line.strip())
		all_numbs.append(number)
		if len(preamble) < preamble_count:
			preamble.append(number)
		else:
			s = find_sum(number, preamble)
			if s is None:
				print(number)
			preamble.pop(0)
			preamble.append(number)
		i += 1
	b = find_set(57195069, all_numbs)
	if b is not None:
		l = all_numbs[b[0]:b[1]+1]
		print(max(l))
		print(min(l))
		print(max(l) + min(l))

		# 57195069