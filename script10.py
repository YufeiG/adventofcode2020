#!/usr/bin/env python3
import re

with open('input10.txt', 'r') as f:
	adapters = [int(x.strip()) for x in f]
	adapters.sort()

	one = 0
	three = 0
	previous_x = 0

	consecutive_ones = 0
	groups_of_ones = []
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
			groups_of_ones.append(consecutive_ones)
			consecutive_ones = 0

	print((one) * (three)) # 2048

	product = 1
	for s in groups_of_ones:
		# a difference of s means s + 1 adapters, but we can't
		# remove the outer 2 adapters because they border a difference of 3,
		# so we work with s - 1 adapters that we could potentially remove
		if s == 1:
			continue # do nothing, one 1 between two 3s can never be removed
		elif s == 2 or s == 3:
			product = product * (2**(s - 1))
		elif s == 4:
			product = product * ((2**(s - 1)) - 1) # minus the one case where all three 1s were removed
		else:
			assert False, s
	print(product) # 1322306994176
