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
		return "({})+".format(a)
	if rule_n == "11":
		a = convert_rule_to_regex_patterns("42")
		b = convert_rule_to_regex_patterns("31")
		r = "("
		for i in range(1, 6):
			r += f"({a}){{{i}}}({b}){{{i}}}|" 
		r += f"({a}){{6}}({b}){{6}})" 
		return r

	rule = rules[rule_n]
	m1 = re.fullmatch("([0-9]+) ([0-9]+) \| ([0-9]+) ([0-9]+)", rule)
	m2 = re.fullmatch("([0-9]+) ([0-9]+)", rule)
	m3 = re.fullmatch("([0-9]+)", rule)
	m4 = re.fullmatch("([0-9]+) \| ([0-9]+)", rule)
	if m1 is not None or m2 is not None or m3 is not None or m4 is not None:
		if m3 is not None:
			return convert_rule_to_regex_patterns(m3.group(1))
		if m2 is not None:
			a = convert_rule_to_regex_patterns(m2.group(1))
			b = convert_rule_to_regex_patterns(m2.group(2))
			return a+b
		if m1 is not None:
			assert m1.group(1), rule
			assert m1.group(2), rule
			assert m1.group(3), m1.group(0)
			assert m1.group(4), rule
			a = convert_rule_to_regex_patterns(m1.group(1))
			b = convert_rule_to_regex_patterns(m1.group(2))
			c = convert_rule_to_regex_patterns(m1.group(3))
			d = convert_rule_to_regex_patterns(m1.group(4))

			return "({}{}|{}{})".format(a,b,c,d)
		if m4 is not None:
			a = convert_rule_to_regex_patterns(m4.group(1))
			b = convert_rule_to_regex_patterns(m4.group(2))
			return "({}|{})".format(a, b)
		assert False
	else:
		# maybe a base rule?
		assert rule_n in base_rules
		return base_rules[rule_n]


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
		if r not in base_rules and r not in regex_patterns:
			reg = convert_rule_to_regex_patterns(r)
			regex_patterns[r] = reg
	rule_to_check = regex_patterns["0"]

	n = 0
	for x in inputs:
		m = re.fullmatch("{}".format(rule_to_check), x)
		if m is not None:
			n += 1
	print(n)
