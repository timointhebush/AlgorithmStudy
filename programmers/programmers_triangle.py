def solution(triangle):
    for level in range(1, len(triangle)):
        for idx_level in range(len(triangle[level])):
            if idx_level == 0:
                triangle[level][idx_level] += triangle[level-1][idx_level]
            elif idx_level == len(triangle[level])-1:
                triangle[level][idx_level] += triangle[level-1][idx_level-1]
            else:
                triangle[level][idx_level] += max(triangle[level-1][idx_level-1], triangle[level-1][idx_level])
    return max(triangle[len(triangle)-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))