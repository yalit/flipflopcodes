from collections import deque
from functools import cache, reduce

def solution_1(lines: list[str]):
    nodes, _, start, end, _, _ = get_grid(lines)

    to_visit = deque([(start,0)])
    visited = set()

    while to_visit:
        pos, n = to_visit.popleft()

        if pos == end:
            return n

        for dr,dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr,nc = pos[0]+dr, pos[1]+dc
            if (nr,nc) in nodes and (nr,nc) not in visited:
                to_visit.append(((nr,nc), n+1))

        visited.add((pos))

def solution_2(lines: list[str]):
    nodes, walls, start, end,h, w = get_grid(lines)
    l,path = bfs(nodes, walls, start, end, start, (0,0), 0, (start,), (start,))
    display(walls, start, end, path, h,w)
    return l

def solution_3(lines: list[str]):
    pass


def get_grid(lines):
    nodes = set()
    walls = set()
    start,end = (0,0), (0,0)
    w = len(lines[0])
    h = len(lines)

    for r, line in enumerate(lines):
        for c, v in enumerate(line):
            if v != '#':
                nodes.add((r,c))
            if v == 'S':
                start = (r,c)
            if v == 'E':
                end = (r,c)
            if v == '#':
                walls.add((r,c))

    return tuple(nodes), tuple(walls), start, end, h, w

def get_dir(a,b):
    return (b[0]-a[0], b[1]-a[1])

def is_reverse(a,b):
    return (a[0]+b[0], a[1]+b[1]) == (0,0)

def get_new_pos(pos,dir):
    return pos[0]+dir[0], pos[1]+dir[1]

@cache
def get_corridor(nodes, walls, pos, dir):
    corridor = []
    exits = []

    idx = 0
    while pos in nodes:
        corridor.append(pos)
        walls = []
        if dir == (0,1) or dir == (0,-1):
            walls = [get_new_pos(pos,(1,0)), get_new_pos(pos, (-1,0))]
        else:
            walls = [get_new_pos(pos,(0,1)), get_new_pos(pos, (0,-1))]
        if idx != 0 and any([x in nodes for x in walls]):
            exits.append(idx)
        pos = get_new_pos(pos,dir)
        idx += 1

    return corridor, exits

cache_lengths = {}
def bfs(nodes, walls, start, end, pos, dir, length, full_path = (), path = ()):
    if pos == end:
        return (length, path)

    if (pos,dir) in cache_lengths:
        return cache_lengths[(pos, dir)]

    lengths = []
    for n_dir in [(0,1), (1,0), (0,-1), (-1,0)]:
        n_pos = get_new_pos(pos, n_dir)

        if not(n_pos in nodes and n_pos not in full_path):
            continue
        
        if n_dir != dir or pos == start:
            corridor, exits = get_corridor(nodes, walls, pos, n_dir)
            c_end = corridor[-1]
            if c_end not in full_path:
                lengths.append(bfs(nodes, walls, start, end, c_end, n_dir, length+1, full_path+tuple(corridor[1:]), path+(c_end,)))

            for e in [x for x in exits if x < len(corridor) - 1]:
                c_end = corridor[e]
                if c_end not in full_path:
                    print("Exit",pos, n_dir, e, corridor)
                    lengths.append(bfs(nodes, walls, start, end, c_end, n_dir, length+e, full_path+tuple(corridor[1:e+1]), path+tuple(corridor[1:e+1])))
        else:
            lengths.append(bfs(nodes, walls, start, end, n_pos, n_dir, length+1, full_path+(n_pos,), path+(n_pos,)))
    
    lengths = [(x,p) for x,p in lengths if x > 0]
    if len(lengths) == 0:
        cache_lengths[(pos,dir)] = (0, path)
    else:
        cache_lengths[(pos,dir)] = reduce(lambda t,x: x if x[0] < t[0] else t, lengths)
    return cache_lengths[(pos, dir)]

def display(walls, start, end, path, height, width):
    for r in range(height):
        line = ''
        for c in range(width):
            p = (r,c)
            if p in walls:
                line += '#'
                continue
            if p == start:
                line += 'S'
                continue
            if p  == end:
                line += 'E'
                continue
            if p in path:
                line += '\e[31mY\e[0m'
                continue
            line += ' '
        print(line)
    
