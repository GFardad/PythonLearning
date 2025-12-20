import re
from tracemalloc import start, stop
from unittest import result


visited = set()
index = 0


def C2I(inp_string):
    if type(inp_string) != str:
        return inp_string
    else:
        char = inp_string[0]
        num = inp_string[1]
        char = (ord(char.lower())) - (ord("a"))
        return (int(char), int(num) - 1)


def calc_offset(x, y):
    offset = [
        [x + 2, y + 1],
        [x + 2, y - 1],
        [x - 2, y + 1],
        [x - 2, y - 1],
        [x + 1, y + 2],
        [x + 1, y - 2],
        [x - 1, y + 2],
        [x - 1, y - 2],
    ]
    offset_t = [tuple(item) for item in offset]
    return tuple(offset_t)


def validator(new_points):
    global visited
    global index
    clean_new_point = []
    for item in new_points:
        if item[0] <= 7 and item[1] <= 7 and item[0] >= 0 and item[1] >= 0:
            clean_new_point.append(item)
    clean_new_point = set(clean_new_point) - visited
    visited.update(clean_new_point)
    index += 1
    return clean_new_point


def main(local_start_point, index):

    new_point = calc_offset(*local_start_point)


def solve(start_cord, stop_cord):
    start_cord = C2I(start_cord)
    stop_cord = C2I(stop_cord)
    queue = [((start_cord), 0)]

    while queue:
        cordinate, dist = queue.pop(0)
        if cordinate == stop_cord:
            return dist
        next_moves = validator(calc_offset(*cordinate))
        for next_move in next_moves:
            queue.append((next_move, dist + 1))


start = input("Give me a number for starting point of BSF : ")
stop = input("Give me a number for targrt point of BSF : ")
result = solve(start, stop)
print(f"shortest path bitwhin {start.upper()} and {stop.upper()} is {result}")
