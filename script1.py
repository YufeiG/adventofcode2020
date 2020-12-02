#!/usr/bin/env python3

def a():
	# initial solution for part1
	with open("input1.txt", "r") as f:
		string = f.read()
		numbs = string.split()
		t = len(numbs)
		for i in range(t):
			for j in range(i+1, t):
				if int(numbs[i]) + int(numbs[j]) == 2020:
					return int(numbs[i])*int(numbs[j])

def b():
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

def c():
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

def d():
	# got rid of inner loop by using a set
	with open("input1.txt", "r") as f:
		string = f.read()
		numbs = [int(x) for x in string.split()]
		numbDict = {}
		t = len(numbs)

		for i, v in enumerate(numbs):
			x = numbDict.get(v, [])
			x.append(i)
			numbDict[v] = x

		numSet = set(numbs)
		for i in range(t):
			for j in range(i+1, t):
				a = numbs[i]
				b = numbs[j]
				s = 2020 - (a + b)

				indices = numbDict.get(s)
				if indices is not None:
					assert len(indices) > 0
					if i in indices:
						indices.remove(i)
					if j in indices:
						indices.remove(j)
					if len(indices) > 0:
						return a*b*s

print(d())