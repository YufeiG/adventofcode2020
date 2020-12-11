#!/usr/bin/env python3
import re

seats = []

# returns number or occupied seats
def check_adjacent_seats(i, j) -> int:
    n = 0
    for x in range(max(0, i-1), min(len(seats), i+2)):
        row = seats[x]
        for y in range(max(0, j-1), min(len(row), j+2)):
            if x == i and j == y:
                continue
            seat = row[y]
            if seat == "#":
                n += 1
    return n

# dir is -1, 0 or 1
def check_is_occupied(i, j, dir_x, dir_y) -> bool:
    x = i
    y = j

    while(True):
        if x < 0 or y < 0:
            break
        if x >= len(seats) or y >= len(seats[0]):
            break

        if x != i or y != j:
            seat = seats[x][y]
            if seat == "#":
                return True
            elif seat == "L":
                return False

        x += dir_x
        y += dir_y

    return False

def check_adjacent_seats_2(i, j) -> int:
    n = 0
    for x in range(-1, 2, 1):
        row = seats[x]
        for y in range(-1, 2, 1):
            if x == 0 and y == 0:
                continue
            if check_is_occupied(i, j, x, y):
                n += 1
    return n


def count_occupied() -> int:
    n = 0
    assert len(seats) == 92
    assert len(seats[0]) == 97
    for i, row in enumerate(seats):
        next_row = []
        for j, seat in enumerate(row):
            if seat == "#":
                n += 1
    return n
    
with open('input11.txt', 'r') as f:
    for line in f:
        assert len(line.strip()) > 0
        seats.append(list(line.strip()))

while(True):
    next_seats = []
    did_change = False
    for i, row in enumerate(seats):
        next_row = []
        for j, seat in enumerate(row):
            if seat == ".":
                next_row.append(".")
            elif seat == "L":
                # check adjacent
                n = check_adjacent_seats_2(i, j)
                if n == 0:
                    next_row.append("#")
                    did_change = True
                else:
                    next_row.append("L")
            else:
                # occupied
                n = check_adjacent_seats_2(i, j)
                if n >= 5:
                    next_row.append("L")
                    did_change = True
                else:
                    next_row.append("#")


        next_seats.append(next_row)

    seats = next_seats

    if did_change is False:
        print(count_occupied())
        exit()
    else:
        print(".")
