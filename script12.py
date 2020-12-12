#!/usr/bin/env python3
import re

# current_dir is N S E or W
# letter is L or R
def rotate_dir(current_dir, letter) -> str:
	all_directions = ["N", "E", "S", "W"]
	i = all_directions.index(current_dir)
	if letter == "L":
		i -= 1
		if i == -1:
			i = len(all_directions) - 1
	elif letter == "R":
		i += 1 
		if i == len(all_directions):
			i = 0
	else:
		assert False
	return all_directions[i]

def rotate_waypoint(current_h, current_v, letter) -> (int, int):
	if letter == "R":
		current_h, current_v = -current_v, current_h
	elif letter == "L":
		current_h, current_v = current_v, -current_h
	else:
		assert False
	return (current_h, current_v)

# (h_change, v_change)
# North is up, -1
# South is down, 1
# East is ->, 1
# west is <-, -1
def dir_amount(current_dir) -> (int, int):
	if current_dir == "N":
		return (0, -1)
	elif current_dir == "E":
		return (1, 0)
	elif current_dir == "S":
		return (0, 1)
	elif current_dir == "W":
		return (-1, 0)
	else:
		assert False

with open('input12.txt', 'r') as f:
	h = 10
	v = -1
	ship_h = 0
	ship_v = 0
	for line in f:
		match = re.match("^([NSEWFLR])([0-9]+)$", line)
		d = match.group(1)
		n = int(match.group(2))

		if d in ["N", "E", "S", "W"]:
			change = dir_amount(d)
			h += change[0]*n
			v += change[1]*n
		elif d in ["L", "R"]:
			times = int(n/90)
			for i in range(times):
				(x, y) = rotate_waypoint(h, v, d)
				h = x
				v = y
		elif d == "F":
			ship_h += h*n
			ship_v += v*n
		else:
			assert False
	print(abs(ship_h)+abs(ship_v))