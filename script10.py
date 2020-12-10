#!/usr/bin/env python3
import re

with open('input10.txt', 'r') as f:
	adapters = [int(x.strip()) for x in f]
	adapters.sort()

	one = 0
	three = 0
	previous_x = 0

	consecutive_ones = 0
	number_of_combinations = 1
	for x in adapters + [adapters[-1] + 3 ]:
		d = x - previous_x
		if d == 1:
			one += 1
		elif d == 3:
			three += 1
		else:
			assert False, d
		previous_x = x

		if d == 1:
			consecutive_ones += 1
		elif consecutive_ones > 0:
			assert consecutive_ones < 5, consecutive_ones
			# a difference of s means s + 1 adapters, but we can't
			# remove the outer 2 adapters because they border a difference of 3,
			# so we work with s - 1 adapters that we could potentially remove
			# if there's only one 1, do nothing, one 1 between two 3s can never be removed
			if consecutive_ones == 2 or consecutive_ones == 3:
				number_of_combinations = number_of_combinations * (2**(consecutive_ones - 1))
			elif consecutive_ones == 4:
				number_of_combinations = number_of_combinations * ((2**(consecutive_ones - 1)) - 1) # minus the one case where all three 1s were removed
			consecutive_ones = 0

	print((one) * (three)) # 2048
	print(number_of_combinations) # 1322306994176
