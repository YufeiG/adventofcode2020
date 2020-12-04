#!/usr/bin/env python3
import re


year_keys = ["byr", "iyr", "eyr"]
mandatory_keys = year_keys + ["hgt", "hcl", "ecl", "pid"]
optional_keys = ["cid"]

def is_field_valid(key, value):
	if key in year_keys:
		if re.match("^[0-9]{4}$", value):
			v = int(value)
			low = {"byr": 1920, "iyr": 2010, "eyr": 2020}
			high = {"byr": 2002, "iyr": 2020, "eyr": 2030}
			if low[key] <= v <= high[key]:
				return True
		return False

	if key == "hgt":
		if value.endswith("cm") or value.endswith("in"):
			v = value[0:-2]
			if re.match("^[0-9]+$", v):
				low = {"cm": 150, "in": 59}
				high = {"cm": 193, "in": 76}
				m = value[-2:]
				g = int(v)
				if low[m] <= g <= high[m]:
					return True
		return False

	if key == "hcl":
		return re.match("^#[0-9a-f]{6}$", value) != None

	if key == "ecl":
		return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

	if key == "pid":
		return re.match("^[0-9]{9}$", value) != None
	if key == "cid":
		return True

	assert False, "Key {} is not recognized".format(key)

def are_all_keys_valid(passport):
	for k, v in passport.items():
		if is_field_valid(k, v) == False:
			return False
	return True

def is_pp_valid(passport):
	all_keys = set(passport.keys())
	inter = all_keys.intersection(set(mandatory_keys))
	if len(inter) == len(mandatory_keys): # all required keys are present
		return are_all_keys_valid(passport)

	if len(inter) < len(mandatory_keys): # some required keys are missing
		return False
	left_over_keys = all_keys - set(mandatory_keys)

	if len(left_over_keys) == 1 and left_over_keys == set(optional_keys): # there's an extra key and it's cid
		return are_all_keys_valid(passport)
	assert False, "Extra unrecognized keys {}".format(left_over_keys)

with open('input4.txt', 'r') as f:
	current_passport = {}
	n = 0
	for line in f:
		if line == "\n":
			if is_pp_valid(current_passport):
				n += 1

			current_passport = {}
		else:
			# parse
			values = line.split(" ")
			for v in values:
				s = v.split(":")
				a = s[0]
				b = s[1]
				assert a not in current_passport
				current_passport[a] = b.strip()

	if is_pp_valid(current_passport):
		n += 1

	print(n)