def solution(expression):
    answer = 0
    numList, oprtList = splitExp(expression)


    return answer

def createOprtCases(oprt):
    n = len(oprt)
    if n == 3:
        n = 6
    elif n == 2:
        n = 4
    else:
        n = 1
    cases = [ {} for i in range(oprt) ]

def cal(a, b, oprt):
    if oprt == "+":
        return a + b
    elif oprt == "*":
        return a * b
    else:
        return a - b         

def splitExp(expression):
    start = 0
    operator = ['-', '*', '+']
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