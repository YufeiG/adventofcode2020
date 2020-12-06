#!/usr/bin/env python3

def intersection(set1, set2) -> set:
	return set1.intersection(set2)

def union(set1, set2) -> set:
	return set1.union(set2)

def process_answer_sets(answer_sets, set_lambda) -> int:
	if len(answer_sets) == 0:
		return 0
	s = answer_sets[0]
	for p in answer_sets[1:]:
		s = set_lambda(s, p)
	return len(s)

with open('input6.txt', 'r') as f:
	t = 0
	people = []
	action = intersection # or union for part 1
	for line in f:
		if line == '\n':
			t += process_answer_sets(people, action)
			people = []
		else:
			current = set()
			for c in line.strip():
				current.add(c)
			people.append(current)

	t += process_answer_sets(people, action)
	print(t)
