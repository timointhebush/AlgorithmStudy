from collections import defaultdict


def solution(record):
    answer = []
    uid_to_name = defaultdict(str)
    for r in record:
        data = r.split(" ")
        if len(data) > 2:
            uid_to_name[data[1]] = data[2]

    for r in record:
        data = r.split(" ")
        name = uid_to_name[data[1]]
        if data[0] == "Enter":
            answer.append(f"{name}님이 들어왔습니다.")
        elif data[0] == "Leave":
            answer.append(f"{name}님이 나갔습니다.")
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))