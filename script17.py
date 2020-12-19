

def count_active_neighbours(cube_pos, cubes):
	# pos is a tuple of 3



def pad(cubes):
	new_cubes = []
	

def cycle(cubes):
	#list[list[list[]]]
	#If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
	#If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
	new_cubes = []
	for i, I in enumerate(cubes):
		new_I = []
		for j, J in enumerate(I):
			new_J = []
			for k, K in enumerate(K):
				n = count_active_neighbours((i, j, k), cubes)
				if K == "#":
					# active
					if n == 2 or n == 3:
						new_J.append("#")
					else:
						new_J.append(".")
				else:
					if n == 3:
						new_J.append("#")
					else:
						new_J.append(".")
			new_I.append(new_J)
		new_cubes.append(new_I)
	return new_cubes

def count_active(cubes):
	ret = 0
	for i in cubes:
		for j in i:
			for k in j:
				if k == "#":
					ret += 1

	return ret

with open('input17.txt', 'r') as f:
	s = 0
	cubes = []

	initial = []
	for line in f:
		row = []
		for c in line:
			row.append(c)
		initial.append(row)
	cubes.append(initial)

	for i in range(6):
		cubes = cycle(cubes)
	print(count_active(cubes))
