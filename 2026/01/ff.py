def solution_1(lines: list[str]):
    return sum([0 if d >= 60 else 60-d for d in [int(x) for x in lines]])

def solution_2(lines: list[str]):
    return sum([0 if d == 60 else (60-d if d < 60 else 5*(d-60)) for d in [int(x) for x in lines]])


def solution_3(lines: list[str]):
    mid = len(lines)//2
    heats = [int(x) for x in lines[:mid]]
    targets = [int(x) for x in lines[mid:]]

    seconds = 0
    for i in range(mid):
        h = heats[i]
        t = targets[i]
        seconds += 0 if h == t else (t-h) if t > h else 5*(h-t) 
    return seconds

