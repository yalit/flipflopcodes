from collections import deque

def solution_1(lines: list[str]):
    gears = process_gears(lines)  
    return get_lights(lines, gears)

def solution_2(lines: list[str]):
    gears = process_gears(lines, True)  
    display = [['.' if lines[r][c] not in ['#', '3', '*', 'S'] else ('*' if lines[r][c] == '*' else gears[(r,c)]) for c in range(len(lines[0]))] for r in range(len(lines))]
    return get_lights(lines, gears)

def solution_3(lines: list[str]):
    gears = process_gears(lines, True, True)  
    return get_lights(lines, gears)


def process_gears(lines, bluetooth = False, prime = False):
    sr,sc = 0,0

    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == 'S':
                sr,sc = r,c

    antennas = {}
    receptors = {}

    if bluetooth:
        for r in range(len(lines)):
            for c in range(len(lines[0])):
                v = lines[r][c]
                if v in list('abcdefghijklmnopqrtuvwxyz'):
                    antennas[(r,c)] = v
                if v in list('ABCDEFGHIJKLMNOPQRTUVWXYZ'):
                    receptors[v] = (r,c)

    if prime:
        for receptor, (r,c) in receptors.items():
            to_visit = deque([(r,c)])
            count = 0
            visited = set()
            while to_visit:
                br,bc = to_visit.popleft()
                if lines[br][bc] == '3' and (br,bc) not in visited:
                    count+=1
                for dr,dc in [(0,1), (0,-1),(1,0),(-1,0)]:
                    nbr,nbc = br+dr,bc+dc
                    if (nbr,nbc) in visited:
                        continue
                    if 0<=nbr<len(lines) and 0<=nbc<len(lines[0]):
                        if lines[nbr][nbc] == '3':
                            to_visit.append((nbr,nbc))
                visited.add((br,bc))

            if is_prime(count):
                to_delete = None
                for pos,a in antennas.items():
                    if a == receptor.lower():
                        to_delete = pos
                if to_delete:
                    del antennas[to_delete]

    to_visit = deque([(sr,sc, 0)])
    visited = set()
    gears = {}
    while to_visit:
        r,c,turn = to_visit.popleft()

        if lines[r][c] in ['#', '3', 'S']:
            if turn:
                gears[(r,c)] = 'R'
            else:
                gears[(r,c)] = 'L'

        for dr,dc in [(0,1), (0,-1),(1,0),(-1,0)]:
            nr,nc = r+dr, c+dc
            if (nr,nc) in visited:
                continue

            if 0 <= nr < len(lines) and 0 <= nc < len(lines[0]) and lines[nr][nc] in ['#', '3']:
                to_visit.append((nr,nc,1-turn))

            if bluetooth and (nr,nc) in antennas:
                rr,rc = receptors[antennas[(nr,nc)].upper()]
                to_visit.append((rr,rc,turn))

        visited.add((r,c,))
    return gears

def get_lights(lines, gears):
    lights = ''
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            l = lines[r][c]
            if l != '*':
                continue
            hl = -1
            neighbors = [(r+1,c), (r-1,c),(r,c+1),(r,c-1)]
            if any(x == 'R' for x in [g for pos,g in gears.items() if pos in neighbors]):
                hl = 1

            if any(x == 'L' for x in [g for pos,g in gears.items() if pos in neighbors]):
                hl = 0

            lights += str(hl) if hl >= 0 else ''

    return int(lights, 2)


def is_prime(n):
    for x in range(2,n):
        if n%x == 0:
            return False
    return True
