#!/usr/bin/env python3

with open('input3.txt', 'r') as f:
    a = f.read()
    map = [list(x) for x in a.split('\n')]


def check(right, down) -> int:
    i = right
    j = down
    t = 0
    while(j < len(map)):
        r = map[j]
        if len(r) == 0:
            break
        if i >= len(r):
            i = i - len(r)
        value = r[i]
        if value == '#':
            t += 1
        i += right
        j += down
    return t

a = check(1, 1)
b = check(3, 1)
c = check(5, 1)
d = check(7,1)
e = check(1,2)
print(b)
print(a*b*c*d*e)