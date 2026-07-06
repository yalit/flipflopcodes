def solution_1(lines: list[str]):
    rc = lines[0]

    h = 0
    m = 0
    for c in rc:
        h += 1 if c == '^' else -1
        m = max(m, h)

    return m

def solution_2(lines: list[str]):
    rc = lines[0]

    h = 0
    m = 0
    up = 0
    down = 0
    for c in rc:
        if c == '^':
            down = 0
            up += 1
            h += up
        else:
            up = 0
            down += 1
            h -= down
        m = max(m, h)

    return m


def solution_3(lines: list[str]):
    rc = lines[0]

    h = 0
    m = 0
    up = 0
    down = 0
    for c in rc:
        if c == '^':
            if down != 0:
                h -= fib(down)
                down = 0
            up += 1
        else:
            if up != 0:
                h += fib(up)
                up = 0
            up = 0
            down += 1
        m = max(m, h)

    if up != 0:
        h += fib(up)
    if down != 0:
        h -= fib(down)

    m = max(m,h)
    return m


f = {0: 0, 1: 1}
def fib(n: int) -> int:
    if n in f:
        return f[n]

    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]
