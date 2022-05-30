def solution(arrows):
    answer = 0
    routes = set()
    points = set()
    points.add((0, 0))
    x, y = 0, 0
    for arrow in arrows:
        dx, dy = get_delta(arrow)
        mx, my = x + dx, y + dy
        nx, ny = x + 2 * dx, y + 2 * dy
        if (mx, my) in points and ((x, y), (mx, my)) not in routes:
            answer += 1
        if (nx, ny) in points and ((mx, my), (nx, ny)) not in routes:
            answer += 1
        routes.add(((x, y), (mx, my)))
        routes.add(((mx, my), (x, y)))
        routes.add(((mx, my), (nx, ny)))
        routes.add(((nx, ny), (mx, my)))
        points.add((mx, my))
        points.add((nx, ny))
        x, y = nx, ny
    return answer


def get_delta(arrow):
    delta = {
        0: (0, 1),
        1: (1, 1),
        2: (1, 0),
        3: (1, -1),
        4: (0, -1),
        5: (-1, -1),
        6: (-1, 0),
        7: (-1, 1),
    }
    return delta[arrow]


print(solution([2, 4, 6, 4, 0, 2, 0, 6]))
print(solution([2, 4, 6, 0, 3, 6, 0, 2, 5]))
