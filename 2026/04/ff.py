from functools import reduce

def solution_1(lines: list[str]):
    cut = 8 if len(lines) < 100 else 400

    return len([x for x in lines[:-cut] if 'o' in x])

def solution_2(lines: list[str]):
    lines = [x for x in lines[::-1] if x != '  |']

    changes = 0
    side = lines[0]
    for l in lines[1:]:
        if l != side:
            changes +=1
            side =l 

    return changes
        


def solution_3(lines: list[str]):
    lines = [x for x in lines[::-1] if x != '  |'] + ["@"]

    workers = 0
    while len(lines) > 1:
        current = lines[0]

        for i,l in enumerate(lines):
            if l == current:
                continue
            else:
                lines[i-1] = '  |'
                current = l
        workers +=1
        lines = [x for x in lines if x != '  |']

    return workers
    

def get_side(leaf):
    if leaf[-3:] == '|-o':
        return 1
    elif leaf[:3] == 'o-|':
        return -1
    return 0
