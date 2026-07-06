import re

def solution_1(lines: list[str]):
    total = 0
    for banana in lines:
        total += get_score(banana)
    return total

def solution_2(lines: list[str]):
    total = 0
    for banana in lines:
        score = get_score(banana)
        total += score if score % 2 == 0 else 0
    return total


def solution_3(lines: list[str]):
    total = 0
    for banana in lines:
        score = get_score(banana)
        ne = len(re.findall(r"(ne)", banana))
        total += score if ne == 0 else 0
    return total


def get_score(banana: str) -> int:
        bas = len(re.findall(r"(ba)",banana))
        return bas + len(re.findall(r"(n[a|e])",banana))
