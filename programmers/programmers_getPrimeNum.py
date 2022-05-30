import math
def solution(numbers):
    numbers = list(numbers)
    checked = [False for i in range(len(numbers))]
    numberSet = set()
    getNums(0, numbers, checked, numberSet, [])
    return getNumOfPrimeNum(numberSet)

def getNums(depth, numbers, checked, numberSet, strNum):
    if depth == len(numbers):
        pass
    else:
        for idx in range(len(numbers)):
            if checked[idx] == False:
                checked[idx] = True
                strNum.append(numbers[idx])
                numberSet.add(int("".join(strNum)))
                getNums(depth+1, numbers, checked, numberSet, strNum)
                strNum.pop()
                checked[idx] = False

def getNumOfPrimeNum(numberSet):
    count = 0
    for num in numberSet:
        primeNum = True
        if num == 0 or num == 1:
            pass
        else:
            for divider in range(2, int(math.sqrt(num)+1 )):
                if num % divider == 0:
                    primeNum = False
                    break
            if primeNum == True:
                count += 1
    return count
            

print(solution("011"))