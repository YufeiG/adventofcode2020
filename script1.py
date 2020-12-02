#!/usr/bin/env python3

def a() -> int:
	# initial solution for part1
	with open("input1.txt", "r") as f:
		string = f.read()
		numbs = string.split()
		t = len(numbs)
		for i in range(t):
			for j in range(i+1, t):
				if int(numbs[i]) + int(numbs[j]) == 2020:
					return int(numbs[i])*int(numbs[j])

def b() -> int:
	# initial solution for part2
	with open("input1.txt", "r") as f:
		string = f.read()
		numbs = string.split()
		t = len(numbs)
		for i in range(t):
			for j in range(i+1, t):
				for k in range(j+1, t):
					if int(numbs[i]) + int(numbs[j]) + int(numbs[k]) == 2020:
						return int(numbs[i])*int(numbs[j])*int(numbs[k])

def c() -> int:
	# made it faster by casting to int up front
	with open("input1.txt", "r") as f:
		string = f.read()
		numbs = [int(x) for x in string.split()]
		t = len(numbs)
		for i in range(t):
			for j in range(i+1, t):
				for k in range(j+1, t):
					if numbs[i] + numbs[j] + numbs[k] == 2020:
						return numbs[i]*numbs[j]*numbs[k]

def d() -> int:
	from collections import defaultdict

	# got rid of inner loop by using a dict
	with open("input1.txt", "r") as f:
		numbs = [int(x) for x in f.read().split()]
		numbDict = defaultdict(set)
		for i, v in enumerate(numbs):
			numbDict[v].add(i)

		for i in range(len(numbs)):
			for j in range(i+1, len(numbs)):
				s = 2020 - (numbs[i] + numbs[j])
				indices = numbDict.get(s)
				# a value exists that sum to 2020
				# check if this is a value we already are using
				if indices is not None and len(indices.difference(set([i, j]))) > 0:
					return numbs[i]*numbs[j]*s

print(d())