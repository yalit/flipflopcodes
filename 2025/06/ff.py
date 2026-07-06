def solution_1(lines: list[str]):
    s = 8 if len(lines) == 6 else 1000
    p = (2,5) if len(lines) == 6 else (250, 749)

    speeds = [tuple(map(int, line.split(","))) for line in lines]
    birds = [(0,0) for _ in lines]

    birds = [((x + 100*speeds[i][0]) % s, (y + 100*speeds[i][1]) % s) for i,(x,y) in enumerate(birds)]

    return len([(x,y) for (x,y) in birds if p[0] <= x <= p[1] and p[0] <= y <= p[1]])
    

def solution_2(lines: list[str]):
    s = 8 if len(lines) == 6 else 1000
    p = (2,5) if len(lines) == 6 else (250, 749)

    speeds = [tuple(map(int, line.split(","))) for line in lines]
    birds = [(0,0) for _ in lines]

    total = 0
    for _ in range(1000):
        birds = [((x + 3600*speeds[i][0]) % s, (y + 3600*speeds[i][1]) % s) for i,(x,y) in enumerate(birds)]
        total += len([(x,y) for (x,y) in birds if p[0] <= x <= p[1] and p[0] <= y <= p[1]])

    return total

def solution_3(lines: list[str]):
    s = 8 if len(lines) == 6 else 1000
    p = (2,5) if len(lines) == 6 else (250, 749)

    speeds = [tuple(map(int, line.split(","))) for line in lines]
    birds = [(0,0) for _ in lines]

    total = 0
    for _ in range(1000):
        birds = [((x + 31556926*speeds[i][0]) % s, (y + 31556926*speeds[i][1]) % s) for i,(x,y) in enumerate(birds)]
        total += len([(x,y) for (x,y) in birds if p[0] <= x <= p[1] and p[0] <= y <= p[1]])

    return total

