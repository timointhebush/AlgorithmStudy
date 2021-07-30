def solution(expression):
    answer = 0
    numList, oprtList = splitExp(expression, ["*", "+", "-"])
    cases, operator = createOprtCases(list(set(oprtList)))
    for case in cases:
        numListCopy, oprtListCopy = numList.copy(), oprtList.copy()
        for idx in case:
            opt = operator[idx]
            while True:
                if oprtListCopy.count(opt) == 0:
                    break
                opt_idx = oprtListCopy.index(opt)
                result = cal( numListCopy[opt_idx], numListCopy[opt_idx+1], opt )
                del numListCopy[opt_idx+1]
                del numListCopy[opt_idx]
                del oprtListCopy[opt_idx]
                numListCopy.insert(opt_idx, result)
        if abs(numListCopy[0]) > answer:
            answer = abs(numListCopy[0])
    return answer

def createOprtCases(oprt):
    n = len(oprt)
    if n == 3:
        return [ (0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 1, 0), (2, 0, 1) ], oprt
    elif n == 2:
        return [ (0, 1), (1, 0) ], oprt
    else:
        return [ (0, ) ], oprt

def cal(a, b, oprt):
    if oprt == "+":
        return a + b
    elif oprt == "*":
        return a * b
    else:
        return a - b         

def splitExp(expression, operator):
    start = 0
    numList = []
    oprtList = []
    for end in range(len(expression)):
        if expression[end] in operator:
            numList.append( int(expression[start:end]) )
            oprtList.append( expression[end] )
            start = end+1
    numList.append(int(expression[start:]))
    return numList, oprtList

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
print(solution("200-300-500-600*40+500+500"))
print(solution("2-990-5+2"))
print(solution("2*2"))