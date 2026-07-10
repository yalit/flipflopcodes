def solution_1(lines: list[str]):
    return get_distinct(lines)

def solution_2(lines: list[str]):
    changes = {(r,c): [x for x in ['>','<','^','v'] if x != lines[r][c]] for r in range(1,len(lines)-1) for c in range(1,len(lines[0])-1)}
    grid = [list(line) for line in lines]
    
    max_distinct = 0
    for r in range(1,len(grid)-1):
        for c in range(1, len(grid[0])-1):
            original = grid[r][c]
            for n in changes[(r,c)]:
                grid[r][c] = n
                max_distinct = max(max_distinct,get_distinct(grid))
            grid[r][c] = original

    return max_distinct



def solution_3(lines: list[str]):
    changes = {(r,c): [x for x in ['>','<','^','v'] if x != lines[r][c]] for r in range(1,len(lines)-1) for c in range(1,len(lines[0])-1)}
    grid = [list(line) for line in lines]
    
    max_distinct = 0
    for r in range(1,len(grid)-1):
        for c in range(1, len(grid[0])-1):
            original = grid[r][c]
            for n in changes[(r,c)]:
                grid[r][c] = n
                max_distinct = max(max_distinct,get_distinct_illegal(grid))
            grid[r][c] = original

    return max_distinct


def get_distinct(grid):
    dirs = {
        '>': (0,1),
        '<': (0,-1),
        '^': (-1,0),
        'v': (1,0)
    }

    pos = (0,0)
    visited = set()
    
    while pos not in visited:
        dir = grid[pos[0]][pos[1]]
        dr,dc = dirs[dir]
        visited.add(pos)
        pos = (pos[0]+dr,pos[1]+dc)

    return len(visited)

def get_distinct_illegal(grid):
    dirs = {
        '>': (0,1),
        '<': (0,-1),
        '^': (-1,0),
        'v': (1,0)
    }

    illegal_move = {'>': 'v', 'v': '<', '<': '^', '^': '>'}

    pos = (0,0)
    visited = set()
    illegal = 0
    
    while pos not in visited or illegal < 3:
        if pos in visited:
            if 0 == pos[0] or 0 == pos[1] or len(grid)-1 == pos[0] or len(grid[0])-1 == pos[1]:
                break
            dir = illegal_move[grid[pos[0]][pos[1]]]
            illegal += 1
        else:
            dir = grid[pos[0]][pos[1]]
        dr,dc = dirs[dir]
        visited.add(pos)
        pos = (pos[0]+dr,pos[1]+dc)

    return len(visited)
