from functools import cache
from collections import deque

def solution_1(lines: list[str]):
    total = 0
    for line in lines:
        w,h = map(int,line.split())

        to_visit = [(0,0)]
        while to_visit:
            pos = to_visit.pop()

            if pos == (w-1, h-1):
                total += 1
                continue

            if pos[0] >= w or pos[1] >= h:
                continue

            for dx,dy in [(0,1), (1,0)]:
                to_visit.append((pos[0]+dx, pos[1]+dy))

    return total

def solution_2(lines: list[str]):
    total = 0
    for line in lines:
        w,h = map(int,line.split())

        total += nb_path_3d((0,0,0),w,h)

    return total


def solution_3(lines: list[str]):
    total = 0
    for line in lines:
        d,s = map(int,line.split())

        total += nb_path_xd(tuple(0 for _ in range(d)), d, s)

    return total

@cache
def nb_path_3d(pos, w, h) -> int:
    target = (w-1, h-1, w-1)
    deltas = [(0,0,1), (0,1,0),(1,0,0)]
    
    if pos == target:
        return 1

    if pos[0] >= w or pos[1] >= h or pos[2] >= w:
        return 0

    total = 0
    for dx, dy, dz in deltas:
        total += nb_path_3d((pos[0]+dx, pos[1]+dy,pos[2]+dz), w, h)

    return total

@cache
def nb_path_xd(pos, d, s) -> int:
    target = tuple(s-1 for _ in range(d))
    deltas = [tuple(1 if x == i else 0 for x in range(d)) for i in range(d)]
    
    if pos == target:
        return 1

    if any(p >= s for p in pos):
        return 0

    total = 0
    for delta in deltas:
        total += nb_path_xd(tuple(p+delta[i] for i,p in enumerate(pos)), d, s)

    return total
