from collections import defaultdict, deque

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def solution(arrows):
    answer = 0
    r, c = 0, 0
    q = deque()
    is_visited_coord = defaultdict(bool)
    is_visited_from_to = defaultdict(bool)

    for arrow in arrows:
        for _ in range(2):
            r, c = r + dr[arrow], c + dc[arrow]
            q.append((r, c))

    r, c = 0, 0
    is_visited_coord[(r, c)] = True
    while q:
        nr, nc = q.popleft()
        if is_visited_coord[(nr, nc)]:
            if not is_visited_from_to[((r, c), (nr, nc))]:
                answer += 1
        else:
            is_visited_coord[(nr, nc)] = True
        is_visited_from_to[((r, c), (nr, nc))] = True
        is_visited_from_to[((nr, nc), (r, c))] = True
        r, c = nr, nc
    return answer


if __name__ == "__main__":
    print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))