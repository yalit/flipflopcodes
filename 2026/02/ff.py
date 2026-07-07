def solution_1(lines: list[str]):
    temps = [0 for _ in range(100)]
    moves = lines[0]

    pos = 0
    for m in moves:
        pos += 1 if m == '>' else -1
        pos = pos % 100
        temps[pos] += 1

    m_temp = (0,0)
    for i, t in enumerate(temps):
        if t > m_temp[1]:
            m_temp = (i+1,t)

    return m_temp[0] * m_temp[1]
    

def solution_2(lines: list[str]):
    moves = lines[0]
    r_moves = "".join(list(reversed(moves)))
    s = len(moves)

    h = 0
    r = 50
    l = 50
    for i in range(s):
        m_l = moves[i]
        m_r = r_moves[i]
        l = (l + (1 if m_l == '>' else -1)) % 100
        r = (r + (1 if m_r == '>' else -1)) % 100
        if l == r:
            h += 1

    return h

def solution_3(lines: list[str]):
    temps = [0 for _ in range(100)]
    moves = lines[0]
    w_moves = list(reversed(moves))

    pos = 0
    delta = 0
    for i, m in enumerate(moves):
        m_w = w_moves[i]
        pos = (pos + (1 if m == '>' else -1)) % 100
        delta += 1 if m_w == '<' else -1
        temps[(pos+delta)%100] += 1

    m_temp = (0,0)
    for i, t in enumerate(temps):
        if t > m_temp[1]:
            m_temp = (i+1,t)

    return m_temp[0] * m_temp[1]
