#!/usr/bin/env python3
import re
bags = { "light red": [(2, 1), (3, 2)], # light red
	1: [(2, 3), (3, 4)], # dark orange
	2: [(4, 1)], # bright white
	3: [(4, 2), (7, 9)], # muted yellow
	4: [(5, 1), (6, 2)], # shiny gold
	5: [(7, 3), (8, 4)], # dark olive
	6: [(7, 5), (8, 6)], # vibrant plum
	7: [], # faded blue
	8: [], # dotted black

}

encoded_bags = {} # {string: {string : int}}
def encode_line(line):
	match = re.match("^([a-z]+ [a-z]+) bags contain ([0-9a-z ,]+).$", line)
	bag_type = match.group(1)
	inner_bag_line = match.group(2)
	if inner_bag_line == "no other bags":
		encoded_bags[bag_type] = {}
		return
	inner_bags = inner_bag_line.split(", ")
	inner_bag_dict = {} # {string: int}
	for inner_bag in inner_bags:
		inner_match = re.match("^([0-9]+) ([a-z]+ [a-z]+) bag[s]?$", inner_bag)
		inner_count = inner_match.group(1)
		inner_bag_name = inner_match.group(2)
		inner_bag_dict[inner_bag_name] = int(inner_count)
	encoded_bags[bag_type] = inner_bag_dict
	print(bag_type)


def can_fit(bag_to_find, bag_type) -> bool:
	inner = encoded_bags[bag_type]
	for inner_bag_type, count in inner.items():
		if inner_bag_type == bag_to_find:
			return True
		else:
			if can_fit(bag_to_find, inner_bag_type):
				return True
	return False


def find_combinations(bag_to_find):
	# returns [str] of other bags that can contain
	ret = []
	for bag_type, inner in encoded_bags.items():
		if can_fit(bag_to_find, bag_type):
			ret.append(bag_type)
	print(ret)
	print(len(ret))

cache = {} # str: int
def count_inner(bag_type) -> int:
	inner = encoded_bags[bag_type]
	if len(inner) == 0:
		return 0

	total = 0
	for inner_bag_type, count in inner.items():
		c = count_inner(inner_bag_type)
		total += c*count + count
	return total




with open('input7.txt', 'r') as f:
	for line in f:
		encode_line(line)
	#find_combinations("shiny gold")
	print(count_inner("shiny gold"))