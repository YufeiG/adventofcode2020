#!/usr/bin/env python3
data_set = []
with open('input3.txt', 'r') as f:
    data_set = [list(x) for x in f.read().split('\n')][:-1] # remove empty value from the split

num_row = len(data_set)
num_col = len(data_set[0])


def check(right, down) -> int:
    num_trees = 0
    col = right
    for row in range(down, num_row, down): # range(start, stop, step)
        if data_set[row][col] == '#':
            # oh look, a tree
            num_trees += 1
        # something about arboreal genetics and biome stability
        col = (col + right) % num_col
    return num_trees

a = check(1, 1)
b = check(3, 1)
c = check(5, 1)
d = check(7,1)
e = check(1,2)
print(b)
print(a*b*c*d*e)