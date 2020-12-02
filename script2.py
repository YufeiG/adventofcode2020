#!/usr/bin/env python3

def a():
	# solution for part 1
	with open("input2.txt", "r") as f:
		string = f.read()
		lines = string.split('\n')
		c = 0
		for line in lines:
			l = line.split(' ')
			if len(l) <= 1:
				continue
			bounds = l[0].split('-')
			lower = int(bounds[0])
			upper = int(bounds[1])
			letter = l[1][0:1]
			pw = l[2]
			count = pw.count(letter)
			if count >= lower and count <= upper:
				c += 1
		print(c)

def b():
	# solution for part 2
	with open("input2.txt", "r") as f:
		string = f.read()
		lines = string.split('\n')
		c = 0
		for line in lines:
			l = line.split(' ')
			if len(l) <= 1:
				continue
			bounds = l[0].split('-')
			lower = int(bounds[0])
			upper = int(bounds[1])
			letter = l[1][0:1]
			pw = l[2]
			a = pw[lower-1] == letter
			b = pw[upper-1] == letter
			if a != b:
				c += 1
		print(c)

b()