def a():
	# initial solution for part1
	with open("input1.txt", "r") as f:
		string = f.read()
		numbs = string.split()
		t = len(numbs)
		for i in range(t):
			for j in range(i+1, t):
				if int(numbs[i]) + int(numbs[j]) == 2020:
					print("num: {}".format(int(numbs[i])*int(numbs[j])))
					exit()

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
						print("num: {}".format(int(numbs[i])*int(numbs[j])*int(numbs[k])))
						exit()
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
						print("num: {}".format(numbs[i]*numbs[j]*numbs[k]))
						exit()

def d():
	# got rid of inner loop by using a set
	with open("input1.txt", "r") as f:
		string = f.read()
		numbs = [int(x) for x in string.split()]
		numSet = set(numbs)
		t = len(numbs)
		for i in range(t):
			for j in range(i+1, t):
				s = 2020 - (numbs[i] + numbs[j])
				if s in numSet:
					print("num: {}".format(numbs[i]*numbs[j]*s))
					exit()

d()