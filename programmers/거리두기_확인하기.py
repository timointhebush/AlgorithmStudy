def solution(places):
    answer = []
    for place in places:
        answer.append(solve(place))
    return answer


def solve(place):
    for r in range(5):
        for c in range(5):
            if place[r][c] == "P":
                if not is_safe(r, c, place):
                    return 0
    return 1


def is_safe(r, c, place):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if nr >= 5 or nr < 0 or nc >= 5 or nc < 0:
            continue
        if place[nr][nc] == "P":
            return False

    dr = [-2, 2, 0, 0]
    dc = [0, 0, -2, 2]
    xdr = [-1, 1, 0, 0]
    xdc = [0, 0, -1, 1]
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        xnr = r + xdr[dir]
        xnc = c + xdc[dir]
        if nr >= 5 or nr < 0 or nc >= 5 or nc < 0:
            continue
        if xnr >= 5 or xnr < 0 or xnc >= 5 or xnc < 0:
            continue
        if place[nr][nc] == "P" and place[xnr][xnc] != "X":
            return False

    dr = [-1, 1, 1, -1]
    dc = [1, 1, -1, -1]
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if nr >= 5 or nr < 0 or nc >= 5 or nc < 0:
            continue
        x1 = (r, nc)
        if x1[0] >= 5 or x1[0] < 0 or x1[1] >= 5 or x1[1] < 0:
            continue
        x2 = (nr, c)
        if x2[0] >= 5 or x2[0] < 0 or x2[1] >= 5 or x2[1] < 0:
            continue
        if place[nr][nc] == "P" and (place[x1[0]][x1[1]] != "X" or place[x2[0]][x2[1]] != "X"):
            return False
    return True


print(solution([
    # ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    # ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))