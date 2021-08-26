def solution(orders, course):
    answer = []
    n = len(orders)
    intersections_cand = []
    for i in range(n):
        for j in range(i+1, n):
            intersection = set(orders[i])&set(orders[j])
            if intersection not in intersections_cand and len(intersection) >= 2:
                intersections_cand.append(intersection)
    intersections_cand = sorted(intersections_cand, key=lambda x : len(x))
    # print(intersections_cand)

    len_cand = {}
    for i in range(course[0], course[-1]+1):
        len_cand[i] = []

    for intersec in intersections_cand:
        num = 0
        for order in orders:
            if intersec & set(order) == intersec:
                num += 1
        len_cand[ len(intersec) ].append( (intersec, num) )
    # print(len_cand)
    
    for c in course:
        cand = len_cand[c]
        if len(cand) != 0:
            max_num = max(cand, key=lambda x : x[1])[1]
            for intersec, num in cand:
                if num == max_num:
                    answer.append( "".join(sorted(list(intersec))) )
    answer.sort()
    return answer

print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["ABCD", "ABCD", "ABCD"], [2,3,4]))
# print(solution(['AB', 'CD','CD','CD','CD','CDE' ], [1, 2, 3]))