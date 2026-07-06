from itertools import product

def solution_1(lines: list[str]):
    trash = [tuple(map(int, line.split(","))) for line in lines]

    total = 0
    l = (0,0)
    for x in trash:
        total += manh(l,x)
        l = x

    return total


def solution_2(lines: list[str]):
    trash = [tuple(map(int, line.split(","))) for line in lines]


    total = 0
    l = (0,0)
    for x in trash:
        d = diag(l,x)
        dx, dy = delta(l,x)
        n = (l[0]+dx*d, l[1]+dy*d)
        total += (d + manh(n,x))
        l = x

    return total

def solution_3(lines: list[str]):
    trash = [tuple(map(int, line.split(","))) for line in lines]
    t_with_manh = [(x, manh((0,0), x)) for x in trash]
    sorted_trash = sorted(t_with_manh, key=lambda a: a[1])

    total = 0
    l = (0,0)
    for x in [x[0] for x in sorted_trash]:
        d = diag(l,x)
        dx, dy = delta(l,x)
        n = (l[0]+dx*d, l[1]+dy*d)
        total += (d + manh(n,x))
        l = x

    return total

def manh(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def diag(a, b):
    return min(abs(a[0] - b[0]), abs(a[1]-b[1]))

def delta(a,b):
    return (-1 if b[0] < a[0] else 1, -1 if b[1] < a [1] else 1)
