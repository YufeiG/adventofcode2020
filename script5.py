#!/usr/bin/env python3
def calculate_num(id_str, char_for_upper, char_for_lower) -> int:
	lower = 0
	upper = 2 ** len(id_str)
	for r in id_str:
		h = (upper + lower)/2.0
		if r == char_for_lower:
			upper = h
		elif r == char_for_upper:
			lower = h
		else:
			assert False
	return int(lower)

def get_seat_id(id_str) -> int:
	assert len(id_str) == 10
	row = calculate_num(id_str[:7], "B", "F")
	col = calculate_num(id_str[7:], "R", "L")
	return row*8 + col

with open('input5.txt', 'r') as f:
	all_ids = [get_seat_id(line.strip()) for line in f]
	all_ids.sort()
	print("Max: {}".format(all_ids[-1]))

	for i, seat_id in enumerate(all_ids[:-1]):
		if seat_id + 2 == all_ids[i+1]:
			print("My seat: {}".format(seat_id + 1))
