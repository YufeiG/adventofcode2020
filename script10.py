#!/usr/bin/env python3
import re

with open('input10.txt', 'r') as f:
	adapters = [int(x.strip()) for x in f]
	adapters.sort()

	one = 0
	three = 0
	previous_x = adapters[0]
	assert previous_x in [1, 2, 3]
	differences = [previous_x]
	for x in adapters[1:]:
		d = x - previous_x
		if d == 1:
			one += 1
		elif d == 3:
			three += 1
		else:
			assert False, d
		differences.append(d)
		previous_x = x
	print((1+one) * (1+three))
	differences.append(3) # the device

	# differences contains 1 or 3
	consec_i = 0
	summed_differences = []
	for i in differences:
		if i == 1:
			consec_i += 1
		elif consec_i > 0:
			summed_differences.append(consec_i-1)
			consec_i = 0

	product = 1
	for s in summed_differences:
		if s == 0:
			continue # do nothing
		elif s == 1 or s == 2:
			product = product * (2**s)
		elif s == 3:
			product = product * ((2 ** s) - 1)
		else:
			assert False, s
	print(product) # 1322306994176
