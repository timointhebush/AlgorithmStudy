def solution(N, number):
    if N == number:
        return 1
    sets = [set() for i in range(8)]
    sets[0] = set([N])
    for numberOfN in range(2, 9):
        for leftSet in range(1, numberOfN):
            rightSet = numberOfN - leftSet
            for calResult1 in sets[leftSet-1]:
                for calResult2 in sets[rightSet-1]:
                    results = getCalculations(calResult1, calResult2)
                    sets[numberOfN-1].update(results)
                    sets[numberOfN-1].add(int(str(N)*numberOfN))
        if number in sets[numberOfN-1]:
            return numberOfN
    return -1

def getCalculations(num1, num2):
    nums = set()
    nums.add(num1 + num2)
    nums.add(num1 - num2)
    nums.add(num1 * num2)
    if num2 != 0:
        nums.add(num1 // num2)
    return nums

print(solution(5, 12))
print(solution(2, 11))