#!/usr/bin/env python3
import re

def multiply_list(myList) :
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x 
    return result 

def part1(bus_and_offset, earliest_time) -> int:
	shortest_time = None
	shortest_n = None
	for (i, bus) in bus_and_offset:
		time = bus - earliest_time%bus
		if shortest_time is None or shortest_time > time:
			shortest_time = time
			shortest_n = bus
	return shortest_n*shortest_time


def part2(bus_and_offset) -> int:
	largest_step_size = None
	largest_step_size_i = None
	for (reference_i, reference_bus) in bus_and_offset:
		bus_numbers_that_leave_with_reference_bus = []
		for (i, bus) in bus_and_offset:
			if i == reference_i:
				continue
			if abs(reference_i - i) == bus:
				bus_numbers_that_leave_with_reference_bus.append(bus)
		step = reference_bus * multiply_list(bus_numbers_that_leave_with_reference_bus)
		if largest_step_size is None or largest_step_size < step:
			largest_step_size = step
			largest_step_size_i = reference_i

	print("Step size: {}".format(largest_step_size))

	n = 0
	while True:
		time_to_check = n*largest_step_size
		if any((time_to_check - largest_step_size_i + i) % bus != 0 for (i, bus) in bus_and_offset):
			n += 1
		else:
			return time_to_check - largest_step_size_i

with open('input13.txt', 'r') as f:
	earliest_time = int(f.readline())
	buses = f.readline().split(",")

	bus_and_offset = [(i, int(bus)) for i, bus in enumerate(buses) if bus != "x"]

	print(part1(bus_and_offset, earliest_time))

	print(part2(bus_and_offset))
