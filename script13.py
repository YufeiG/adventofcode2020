#!/usr/bin/env python3
import re

def multiply_list(myList) :
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x 
    return result 


with open('input13.txt', 'r') as f:
	earliest_time = int(f.readline())
	buses = f.readline().split(",")

	shortest_time = None
	shortest_n = None

	bus_and_offset = []
	first_n = int(buses[0])

	for i, bus in enumerate(buses):
		if bus != "x":
			bus_n = int(bus)
			bus_and_offset.append((i, bus_n))

			time = bus_n - earliest_time%bus_n
			if shortest_time is None or shortest_time > time:
				shortest_time = time
				shortest_n = bus_n
	print(shortest_n*shortest_time) # part 1

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
		skip = False
		for (i, bus) in bus_and_offset:
			if (time_to_check - largest_step_size_i + i) % bus != 0:
				skip = True
				break
		if skip:
			n += 1
		else:
			print(time_to_check - largest_step_size_i) # part 2
			break