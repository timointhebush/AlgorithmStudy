from collections import defaultdict


def solution(participant, completion):
    names = set()
    same_name_to_num = defaultdict(int)
    for c in completion:
        if c not in names:
            names.add(c)
        else:
            same_name_to_num[c] += 1

    for same_name in same_name_to_num.keys():
        same_name_to_num[same_name] += 1

    for p in participant:
        if p not in names:
            return p
        if p in same_name_to_num:
            same_name_to_num[p] -= 1
            if same_name_to_num[p] == 0:
                del same_name_to_num[p]
                names.remove(p)
        else:
            names.remove(p)
    return list(names)[0]