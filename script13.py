#!/usr/bin/env python3
import re
from math import floor, gcd

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

# returns (q1, q2) such that q1*p1 + difference = q2*p2
def calculate_for_pair(p1, p2, difference) -> (int, int):
	p = p1*p2
	assert difference < p
	assert difference >= 0

	if difference == p2:
		return (p2, p1-1)
	if difference == p1:
		return (p2+1, p1)
	for i in range(1, p1):
		s = i*p2
		# find multiple of x_n near it
		m = s%p1

		x_s = s - m
		d = s - x_s
		if d == difference:
			q1 = x_s // p1
			return (q1, i)
	print("p1 {} p2 {} difference {}".format(p1, p2, difference))
	assert False

def calculate_for_pair_with_flex_difference(p1, p2, difference) -> (int, int):
	if difference < 0:
		(a,b) = calculate_for_pair(p2, p1, -difference)
		return (b,a)
	else:
		return calculate_for_pair(p1, p2, difference)

with open('input13.txt', 'r') as f:
	earliest_time = int(f.readline())
	buses = f.readline().split(",")

	print(buses)
	shortest_time = None
	shortest_n = None

	bus_and_offset = []
	for i, bus in enumerate(buses):
		if bus != "x":
			bus_n = int(bus)
			bus_and_offset.append((i, bus_n))

			n = int(floor(earliest_time/bus_n))
			remainder = earliest_time - bus_n*n
			time = bus_n - remainder
			if shortest_time is None or shortest_time > time:
				shortest_time = time
				shortest_n = bus_n
	print(shortest_n*shortest_time)

	bus_and_offset.sort(key=lambda x: x[1])
	print(bus_and_offset)
	(max_i, max_n) = bus_and_offset[-1]
	q_pairs = []
	for (di, pi) in reversed(bus_and_offset[:-1]):
		(q1, qi) = calculate_for_pair_with_flex_difference(max_n, pi, max_i - di)	
		print("p1 {} p2 {} difference {} q1 {} q2 {}".format(max_n, pi, max_i - di, q1, qi))

		q_pairs.append((q1, pi))

	# find in q_pairs where q1*max_n + max_n* pi*h are all equal for integer h
	h = 0
	while True:
		(q1, pi) = q_pairs[0]
		v = q1 + pi*h
		skip = False
		for (Q1, Pi) in q_pairs[1:]:
			vi = Q1 + Pi*h
			if vi != v:
				skip = True
				break
		if skip:
			h += 1
		else:
			print(h)
			exit()

	exit()
	p = x_n*max_n
	d = []
	for j in range(1, x_n + 1):
		s = j*max_n
		# find multiple of x_n near it
		x_s = (s - (s%x_n))
		print(s - x_s)
		d.append(s - x_s)



	d.sort()
	print(d)

	exit()
	i = 1
	while True:
		max_product = max_n * i

		# check
		skip = False
		for t in bus_and_offset[:-1]:
			(i, n) = t
			i_diff = max_i - i
			product_diff = max_product - i_diff
			if product_diff % n != 0:
				skip = True
				break

		if skip:
			i += 1
		else:
			print(max_product)
			print(max_i)
			exit()
