def solution_1(lines: list[str]):
    evolutions = {}
    for l in lines:
        ev = l.split()
        if ev[0] in evolutions:
            continue
        evolutions[ev[0]] = ev[1:]

    stoats = {x:0 for x in evolutions.keys()}

    stoats['A'] = 1
    stoats['B'] = 1

    for i in range(7):
        new_stoats = {x:0 for x in stoats.keys()}
        for s,n in stoats.items():
            if n == 0:
                continue

            for ns in evolutions[s]:
                new_stoats[ns] += n
        stoats = new_stoats

    return sum(stoats.values())

def solution_2(lines: list[str]):
    return solve_p2_3(lines, 7)

def solution_3(lines: list[str]):
    return solve_p2_3(lines, 21)

def solve_p2_3(lines, n):
    evolutions = {}
    for l in lines:
        ev = l.split()
        evolutions["".join(ev[:2])] = "".join(ev[2:])
        evolutions["".join(reversed(ev[:2]))] = "".join(ev[2:])

    stoats = {'AB': 1}

    for _ in range(n):
        new_stoats = {}
        for s,n in stoats.items():
            if s not in evolutions:
                new_stoats[s] = 1 if s not in new_stoats else new_stoats[s] + 1
                continue
            ns = s[0]+evolutions[s]+s[1]

            for i in range(len(ns)-1):
                evolution = ns[i:i+2]
                if evolution not in new_stoats:
                    new_stoats[evolution] = 0
                new_stoats[evolution] += n

        stoats = new_stoats

    return sum(stoats.values()) +1
