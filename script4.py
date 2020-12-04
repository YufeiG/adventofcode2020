#!/usr/bin/env python3
import re


year_keys = ["byr", "iyr", "eyr"]
mandatory_keys = set(year_keys + ["hgt", "hcl", "ecl", "pid"])
optional_keys = set(["cid"])

def is_field_valid(key, value):
	if key in optional_keys:
		return True

	if key in year_keys:
		if re.match("^[0-9]{4}$", value):
			low = {"byr": 1920, "iyr": 2010, "eyr": 2020}
			high = {"byr": 2002, "iyr": 2020, "eyr": 2030}
			return low[key] <= int(value) <= high[key]
		return False

	if key == "hgt":
		match = re.match("^([0-9]+)(cm|in)$", value)
		if match:
			number = int(match.group(1))
			scale = match.group(2)
			low = {"cm": 150, "in": 59}
			high = {"cm": 193, "in": 76}
			return low[scale] <= number <= high[scale]
		return False

	if key == "hcl":
		return re.match("^#[0-9a-f]{6}$", value) != None

	if key == "ecl":
		return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

	if key == "pid":
		return re.match("^[0-9]{9}$", value) != None

	assert False, "Key {} is not recognized".format(key)

def are_all_keys_valid(passport):
	return all([is_field_valid(field_key, field_value) for field_key, field_value in passport.items()])

def is_valid(passport):
	return mandatory_keys.issubset(passport.keys()) and are_all_keys_valid(passport)

def get_passports():
	with open('input4.txt', 'r') as f:
		current_passport = {}
		for line in f:
			if line == "\n":
				yield current_passport
				current_passport = {}
			else:
				values = line.strip().split(" ")
				for value in values:
					fields = value.split(":")
					assert fields[0] not in current_passport, "dup key detected"
					current_passport[fields[0]] = fields[1]
		yield current_passport

num_valid_passports = len([1 for passport in get_passports() if is_valid(passport)])
print(num_valid_passports)