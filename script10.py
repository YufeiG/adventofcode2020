#!/usr/bin/env python3
import re

with open('input10.txt', 'r') as f:
	adapters = []
	for x in f:
		adapters.append(int(x.strip()))
	adapters.sort()
	print(adapters)

	one = 0
	three = 0
	previous_x = adapters[0]
	assert previous_x == 1
	differences = [1]
	for x in adapters[1:]:
		if x - previous_x == 1:
			one += 1
		elif x - previous_x == 3:
			three += 1
		else:
			assert False
		differences.append(x - previous_x)
		previous_x = x
	print((1+one) * (1+three))
	differences.append(3)

	# 
	# differences contains 1 or 3
	# never remove 3
	# we can remove 1, 1,1, or 1,1,1, but never a 3
	# count how many of the 1 patterns there are
	print(differences)
	consec_i = 0
	ones = 0
	b = 0
	num_3s = 0
	c = 0
	summed_differences = []
	for i in differences:
		if i == 1:
			consec_i += 1
		else:
			if consec_i == 0:
				continue
			summed_differences.append(consec_i-1)
			b += (consec_i - 1)
			if consec_i == 1:
				print("single")
			elif consec_i <= 3:
				ones += consec_i - 1
				c += 2 ** (consec_i - 1)
			elif consec_i == 4:
				# calculate how many permutations of i works
				ones += 3
				num_3s += 1
				c += 2 ** (consec_i - 1) - 1

			else:
				assert False, consec_i
			print(consec_i)
			consec_i = 0
	m = b - (3*num_3s)
	print((2**b) - (2**m))
	# not 268435456
	# not 18446744073709551616
	# not 33554432
	# not 268435591
	# not 4294967296
	# not 4398046511104
	# not 4398046478336
	running = 1
	print(summed_differences)
	for s in summed_differences:
		if s == 0:
			print("zero")
		elif s == 1 or s == 2:
			running = running * (2**s)
		elif s == 3:
			p = (2 ** 3) - 1
			running = running * p
		else:
			assert False, s
	print(running)



