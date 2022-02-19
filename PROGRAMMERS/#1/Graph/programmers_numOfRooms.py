def solution(arrows):
    answer = 0
    x, y = 0, 0
    num_visit = {(0,0):1}
    direction = {(0,0):set()}
    for arrow in arrows:
        for _ in range(2):
            direction[(x, y)].add(arrow)
            x, y = getNextCoord(arrow, x, y)
            opposite_arrow = getOpposite(arrow)
            if (x, y) in num_visit:
                if opposite_arrow not in direction[(x, y)]:
                    #방 생성
                    answer += 1
                    direction[(x, y)].add(opposite_arrow)
                else: #이전에 방문한적은 있지만, 같은방향에서 방문
                    pass
                num_visit[(x, y)] += 1
            else: #해당 좌표 첫방문
                num_visit[(x, y)] = 1
                direction[(x, y)] = set([opposite_arrow])
    return answer

def getNextCoord(arrow, x, y):
    if arrow == 0:
        return (x+0, y+1)
    elif arrow == 1:
        return (x+1, y+1)
    elif arrow == 2:
        return (x+1, y+0)
    elif arrow == 3:
        return (x+1, y-1)
    elif arrow == 4:
        return (x+0, y-1)
    elif arrow == 5:
        return (x-1, y-1)
    elif arrow == 6:
        return (x-1, y+0)
    elif arrow == 7:
        return (x-1, y+1)

def getOpposite(arrow):
    if arrow >= 0 and arrow <= 3:
        return arrow + 4
    else:
        return arrow - 4

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
print(solution([6, 5, 2, 7, 1, 4, 2, 4, 6]))
print(solution([5, 2, 7, 1, 6, 3]))
print(solution([6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]))