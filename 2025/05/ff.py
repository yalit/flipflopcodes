def solution_1(lines: list[str]):
    pos = {}
    path = lines[0]

    for i,c in enumerate(path):
        if c not in pos:
            pos[c] = (i,)
        else:
            pos[c] = pos[c] + (i,)

    l,i = (path[0], 0)
    steps = 0
    while i < len(path):
        s,e = pos[l]
        steps += abs(s-e)
        if i == s:
            i = e+1
        else:
            i = s + 1

        if i < len(path):
            l = path[i]

    return steps

def solution_2(lines: list[str]):
    pos = {}
    path = lines[0]

    for i,c in enumerate(path):
        if c not in pos:
            pos[c] = (i,)
        else:
            pos[c] = pos[c] + (i,)

    visited = set()
    l,i = (path[0], 0)
    while i < len(path):
        s,e = pos[l]
        if i == s:
            i = e+1
        else:
            i = s + 1
        visited.add(l)

        if i < len(path):
            l = path[i]

    not_visited = []
    for c in path:
        if c not in visited and c not in not_visited:
            not_visited.append(c)
    return "".join(not_visited)



def solution_3(lines: list[str]):
    pos = {}
    path = lines[0]

    for i,c in enumerate(path):
        if c not in pos:
            pos[c] = (i,)
        else:
            pos[c] = pos[c] + (i,)

    l,i = (path[0], 0)
    steps = 0
    while i < len(path):
        s,e = pos[l]
        steps += abs(s-e) if l.islower() else -1 * abs(s-e)
        if i == s:
            i = e+1
        else:
            i = s + 1

        if i < len(path):
            l = path[i]

    return steps

