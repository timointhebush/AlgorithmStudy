from itertools import product


def solution(info, query):
    answer = []
    db = {}
    for idx, data in enumerate(info):
        data = data.split(" ")
        key = (data[0], data[1], data[2], data[3])
        if key in db:
            db[key].append(data[4])
        else:
            db[key] = [data[4]]
    print(db)

    for q in query:
        tmp = q.split(" ")
        lang, part = tmp[0], tmp[2]
        career, food, score = tmp[4], tmp[6], int(tmp[7])
        option = make_key(lang, part, career, food)
        scores = []
        for key in product(option[0], option[1], option[2], option[3]):
            print("key", key)
            if key not in db:
                pass
            else:
                scores += db[key]
        print(scores)
        print("")
        scores.sort()
        # answer.append(len(scores) - scores.index(score))
    print(answer)


def make_key(lang, part, career, food):
    option = [lang, part, career, food]
    category = [
        ["cpp", "java", "python"],
        ["backend", "frontend"],
        ['junior", "senior'],
        ["chicken", "pizza"],
    ]
    for i in range(4):
        if option[i] == "-":
            option[i] = category[i]
        else:
            option[i] = [option[i]]
    return option


# def dd(scores, target):
#     for i, s in enumerate(scores):
#         if s

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
