def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    set1 = make_set(str1)
    set2 = make_set(str2)
    simil = get_simil(set1, set2)
    return int(simil * 65536)

def make_set(string):
    multi_set = []
    l = len(string)
    for i in range(l - 1):
        j = i + 1
        tmp = string[i] + string[j]
        if tmp.isalpha():
            multi_set.append(tmp)
    return multi_set

def get_simil(set1, set2):
    l1, l2 = len(set1), len(set2)
    if l1 == 0 and l2 == 0:
        return 1
    intersection = []
    for i in range(l1 - 1, -1, -1):
        string1 = set1[i]
        for j in range(len(set2) - 1, -1, -1):
            string2 = set2[j]
            if string1 == string2:
                intersection.append(string1)
                del set1[i]
                del set2[j]
                break
    return len(intersection) / (len(intersection) + len(set1) + len(set2))

print(solution('FRANCE', 'french'))
print(solution('E=M*C^2', 'e=m*c^2'))