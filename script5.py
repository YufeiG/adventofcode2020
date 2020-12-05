#!/usr/bin/env python3

def get_row(row_str):
	upper = 128
	lower = 0
	for r in row_str:
		h = (upper + lower)/2.0
		if r == "F":
			upper = h
		elif r == "B":
			lower = h
		else:
			assert False
	print("{} {}".format(upper, lower))

	return lower

def get_col(col_str):
	upper = 8
	lower = 0
	for r in col_str:
		h = (upper + lower)/2.0
		if r == "L":
			upper = h
		elif r == "R":
			lower = h
		else:
			assert False
	print("{} {}".format(upper, lower))

	return lower

def get_num(id_str):
	assert len(id_str) == 10
	first = id_str[:7]
	second = id_str[7:]
	print(first)
	print(second)
	row = get_row(first)
	col = get_col(second)
	return row*8 + col

with open('input5.txt', 'r') as f:
	max_numb = 0
	all_ids = []
	for r in f:
		id_str = get_num(r.strip())
		print(id_str)
		all_ids.append(id_str)
		if id_str > max_numb:
			max_numb = id_str
	print(max_numb)
	all_ids.sort()

	for i, seat_id in enumerate(all_ids):
		if i > 0 and i < len(all_ids) - 1:
			before = all_ids[i-1]
			after = all_ids[i+1]
			if seat_id + 2 == after:
				print(seat_id + 1)
			if seat_id - 2 == before:
				print(seat_id - 1)

