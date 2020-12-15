#!/usr/bin/env python3
import re

puzzle_input = "2,0,1,9,5,19".split(",")

last_spoken_dict = {}
for i, n in enumerate(puzzle_input):
	last_spoken_dict[int(n)] = [i]

last_spoken = int(puzzle_input[-1])

# starts at 0, though the puzzle is asking for player number starting at 1
# so we want the 2019th spoken
for current_player in range(len(puzzle_input), 30000000):
	current_spoken = 0
	if last_spoken in last_spoken_dict:
		last_array = last_spoken_dict[last_spoken]
		if len(last_array) > 1:
			current_spoken = last_array[-1] - last_array[-2]

	if current_spoken not in last_spoken_dict:
		last_spoken_dict[current_spoken] = []
	last_spoken_dict[current_spoken].append(current_player)

	last_spoken = current_spoken
	if len(last_spoken_dict[current_spoken]) > 2:
		last_spoken_dict[current_spoken] = last_spoken_dict[current_spoken][-2:]

print(last_spoken)