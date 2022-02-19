def solution(s):
    answer = []
    splitted = s.split("},{")
    splitted[0] = splitted[0].replace("{{", "")
    splitted[-1] = splitted[-1].replace("}}", "")
    for i in range(len(splitted)):
        splitted[i] = set(splitted[i].split(","))
    splitted = sorted(splitted, key=lambda x: len(x))
    answer.append(int(list(splitted[0])[0]))
    for i in range(len(splitted) - 1):
        diff_set = splitted[i + 1] - splitted[i]
        answer.append(int(list(diff_set)[0]))
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
