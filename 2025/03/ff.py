
from functools import reduce


def solution_1(lines: list[str]):
    c = {}

    for b in lines:
        if b not in c:
            c[b] = 0
        c[b] += 1

    m = 0
    mb = ""
    for b,n in c.items():
        if n > m:
            m = n
            mb = b

    return(mb)

def solution_2(lines: list[str]):
    greens = 0

    for bush in lines:
        r,g,b = bush.split(',')
        uniques = reduce(lambda a,x: a if x in a else a + (x,) , [r,g,b],())
        if len(uniques) < 3:
            continue
        if g > r and g > b:
            greens+=1

    return greens


def solution_3(lines: list[str]):
    price = 0

    for bush in lines:
        r,g,b = bush.split(',')
        uniques = reduce(lambda a,x: a if x in a else a + (x,) , [r,g,b],())
        if len(uniques) < 3:
            price += 10
        elif g > r and g > b: #green
            price += 2
        elif r > g and r > b: #red
            price += 5
        elif b > r and b > g: #green
            price += 4

    return price 

