#!/usr/bin/env python3
import re

regex_patterns = {}
rules = {}
base_rules = {}

#	rules["8"] = "42 | 42 8"
#	rules["11"] = "42 31 | 42 11 31"
def convert_rule_to_regex_patterns(rule_n):
	if rule_n == "8":
		a = convert_rule_to_regex_patterns("42")
		return f"({a})+"

	if rule_n in base_rules:
		return base_rules[rule_n]
	rule = rules[rule_n]

	if rule_n == "11":
		rule = "42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 31"

	ors = rule.split("|")
	values = []
	for o in ors:
		ns = o.strip().split(" ")
		values.append("".join([convert_rule_to_regex_patterns(x) for x in ns]))
	s = "|".join(values)
	return f"({s})"

def generate_base_rules():
	for r, v in rules.items():
		m = re.fullmatch("\"([a-z]{1})\"", v)
		if m:
			base_rules[r] = m.group(1)
	return base_rules


with open('input19.txt', 'r') as f:
	at_inputs = False
	inputs = []
	for line in f:
		if line == "\n":
			at_inputs = True
			continue
		if at_inputs:
			inputs.append(line.strip())
		else:
			m = re.fullmatch("([0-9]+): ([0-9\"| a-z]+)", line.strip())
			assert m, line
			rules[m.group(1)] = m.group(2)
	rules["8"] = "42 | 42 8"
	rules["11"] = "42 31 | 42 11 31"

	generate_base_rules()

	for r, v in rules.items():
		if r not in base_rules:
			reg = convert_rule_to_regex_patterns(r)
			regex_patterns[r] = reg

	rule_to_check = regex_patterns["0"]

	n = 0
	for x in inputs:
		m = re.fullmatch(rule_to_check, x)
		if m is not None:
			n += 1
	print(n)
