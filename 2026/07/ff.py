def solution_1(lines: list[str]):
    pos = (0,0)
    movements = lines[0][:len(lines[0])//2]
    i = 2
    target = tuple(map(int, lines[i].split(',')))
    count = 0

    for m in movements:
        pos = move(pos, m)
        if pos == target:
            count += 1
            i += 1
            target = tuple(map(int, lines[i].split(',')))


    return count



def solution_2(lines: list[str]):
    movements = lines[0]
    i = 2
    target = tuple(map(int, lines[i].split(',')))
    snake = tuple([(0,0)])

    for m in movements:
        pos = move(snake[0],m)
        if pos in snake[:-1]:
            break

        if pos != target:
            snake = (pos,)+snake[:-1]
        
        if pos == target:
            i += 1
            target = tuple(map(int, lines[i].split(',')))
            snake = (pos,)+snake
    
    return len(snake) 



def solution_3(lines: list[str]):
    movements = lines[0]
    i = 2
    target = tuple(map(int, lines[i].split(',')))
    snake = tuple([(0,0)])
    count = 0

    for m in movements:
        pos = move(snake[0],m)
        if pos in snake[:-1]:
            snake = snake[:snake[:-1].index(pos)]
            count +=1

        if pos != target:
            snake = (pos,)+snake[:-1]
        
        if pos == target:
            i += 1
            target = tuple(map(int, lines[i].split(','))) if i < len(lines) else None
            snake = (pos,)+snake
    
    return len(snake) * count

def move(pos, m):
    moves = {'>': (1,0), '<': (-1,0), '^': (0,1), 'v': (0,-1)}
    return (pos[0]+moves[m][0], pos[1]+moves[m][1])
