def solution(participant, completion):
    sum_hash = 0
    dict_participant = {}
    for name in participant:
        dict_participant[hash(name)] = name
        sum_hash += hash(name)
    for name in completion:
        sum_hash -= hash(name)
    return dict_participant[sum_hash]