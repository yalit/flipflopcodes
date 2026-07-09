import re

low= r"([a-z])"
up= r"([A-Z])"
dig= r"([0-9])"

def solution_1(lines: list[str]):
    max_score = (0, "")

    for line in lines:
        score = get_score_1(line) * len(line)

        if score > max_score[0]:
            max_score = (score, line)

    return max_score[1]

def solution_2(lines: list[str]):
    max_score = (0, "")

    for line in lines:
        score = get_score_2(line)

        score *= len(line)
        if score > max_score[0]:
            max_score = (score, line)

    return max_score[1]


def solution_3(lines: list[str]):
    charactersToAdd = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ7'

    m_score = 0
    for c in charactersToAdd:
        score = sum([get_score_2(line+c)*(len(line)+1) for line in lines]) 
        m_score = max(m_score, score)

    return m_score

def get_score_1(line):
    score = 0

    if (len(re.findall(low, line))) > 0:
        score+=1
    if (len(re.findall(up, line))) > 0:
        score+=1
    if (len(re.findall(dig, line))) > 0:
        score+=1
    return score

def get_score_2(line):
    score = get_score_1(line)

    # 7
    digits = re.findall(dig, line)
    if len(digits) > 0 and len([x for x in digits if x != "7"]) == 0:
        score += 7

    # sequence
    sequences = {}
    current = ""
    for c in line:
        if c not in sequences:
            sequences[c] = [1]
            current = c
        else:
            if c == current:
                sequences[c][-1] += 1
            else:
                sequences[c].append(1)
                current = c
    candidates = [max(n) for n in sequences.values() if max(n) >= 3]
    if len(candidates) > 0:
        score += (max(candidates)**2)

    if has_colors(line):
        score *= 3

    return score

def has_colors(line):
    return len(re.findall(r"(red|green|blue)", line)) > 0
