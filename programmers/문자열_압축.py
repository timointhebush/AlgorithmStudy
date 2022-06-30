def solution(s):
    len_s = len(s)
    answer = len_s
    for len_unit in range(1, (len_s // 2) + 1):
        left = s[0:len_unit]
        idx = len_unit
        unit = left
        print("unit", unit)
        cnt = 1
        tmp_str = ""
        while idx <= len_s - len_unit:
            right = s[idx:idx + len_unit]
            if left == right:
                cnt += 1
            else:
                tmp_str = add_unit(tmp_str, cnt, unit)
                unit = right
                cnt = 1
            left = right
            idx += len_unit
        tmp_str = add_unit(tmp_str, cnt, unit)
        tmp_str += s[idx:]
        print(tmp_str)
        if len(tmp_str) < answer:
            answer = len(tmp_str)
    return answer


def add_unit(tmp_str, cnt, unit):
    if cnt == 1:
        tmp_str += unit
    else:
        tmp_str += (str(cnt) + unit)
    return tmp_str


print(solution("ababcdcdababcdcd"))