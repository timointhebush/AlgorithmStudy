from itertools import product


def solution(info, query):
    answer = []
    db = {}
    for i in info:
        tmp = i.split(" ")
        cases = product((tmp[0], "-"), (tmp[1], "-"), (tmp[2], "-"), (tmp[3], "-"))
        for case in cases:
            if case in db:
                db[case].append(int(tmp[4]))
            else:
                db[case] = [int(tmp[4])]

    for q in query:
        tmp = q.split(" ")
        key = (tmp[0], tmp[2], tmp[4], tmp[6])
        if key in db:
            scores = sorted(db[key])
            # print(scores)
            # print("target:", tmp[7])
            idx = binary_search(scores, 0, len(scores) - 1, int(tmp[7]))
            answer.append(len(scores) - idx)
        else:
            answer.append(0)
    return answer


def binary_search(scores, start, end, target):
    if start >= end:
        return start
    mid = (start + end) // 2
    if scores[mid] == target:
        return mid
    elif scores[mid] > target:
        return binary_search(scores, start, mid - 1, target)
    else:
        return binary_search(scores, mid + 1, end, target)


print(
    solution(
        [
            "java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50",
        ],
        [
            "java and backend and junior and pizza 100",
            "python and frontend and senior and chicken 200",
            "cpp and - and senior and pizza 250",
            "- and backend and senior and - 150",
            "- and - and - and chicken 100",
            "- and - and - and - 150",
        ],
    )
)
