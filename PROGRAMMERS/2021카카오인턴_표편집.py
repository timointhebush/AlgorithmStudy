def solution(n, k, cmd):
    answer = ''
    stack = []
    table = [_ for _ in range(n)]
    idx = k
    for c in cmd:
        if c[0] == "U":
            idx -= toNum(c)
        elif c[0] == "D":
            idx += toNum(c)
        elif c[0] == "C":
            stack.append( (idx, table[idx]) )
            del table[idx]
            if idx == len(table):
                idx -= 1
            else:
                pass
        elif c[0] == "Z":
            d_idx, d_name = stack.pop()
            table.insert(d_idx, d_name)
            if d_idx <= idx:
                idx += 1
    print(table)
    idx = 0
    for value in table:
        if idx == value:
            idx += 1
            answer += 'O'
        else:
            while idx < value:
                idx +=1
                answer += 'X'
            idx += 1
            answer += 'O'
    return answer

def toNum(c):
    tmp = c.split(" ")
    return int(tmp[1])

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))