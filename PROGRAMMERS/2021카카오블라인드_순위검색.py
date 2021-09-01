from itertools import combinations, product
from bisect import bisect_left


def make_all_cases(separate_info):
    cases = []
    for k in range(5):
        for condition in combinations([0, 1, 2, 3], k):
            case = []
            for idx in range(4):
                if idx not in condition:
                    case.append(separate_info[idx])
                else:
                    case.append("-")
            cases.append("".join(case))
    return cases


def solution(info, query):
    answer = []
    db = {}
    for i in info:
        tmp = i.split(" ")
        cases = make_all_cases(tmp)
        # print(cases)
        for case in cases:
            if case in db:
                db[case].append(int(tmp[4]))
            else:
                db[case] = [int(tmp[4])]

    for q in query:
        tmp = q.split(" ")
        key = (tmp[0], tmp[2], tmp[4], tmp[6])
        key = "".join(key)
        # print(key)
        if key in db:
            scores = sorted(db[key])
            # print(scores)
            # print("target:", tmp[7])
            idx = bisect_left(scores, int(tmp[7]))
            answer.append(len(scores) - idx)
        else:
            answer.append(0)
    return answer


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
