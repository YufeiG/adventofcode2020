#!/usr/bin/env python3



with open('input6.txt', 'r') as f:
	t = 0

	people = []
	for line in f:
		if line == '\n':
			# process
			if len(people) == 0:
				continue
			s = people[0]
			for i, p in enumerate(people[1:]):
				s = s.intersection(p)

			t += len(s)
			people = []
		else:
			current = set()
			for c in line.strip():
				current.add(c)
			people.append(current)
	if len(people) > 0:
		s = people[0]
		for i, p in enumerate(people[1:]):
			s = s.intersection(p)
		t += len(s)
	print(t)
