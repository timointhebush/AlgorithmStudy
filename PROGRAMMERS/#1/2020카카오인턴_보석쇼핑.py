def solution(gems):
    ans = []
    l, r = 0, 0
    numOfKind, numOfGem = len(set(gems)), {gems[r] : 1}
    lenOfDis = len(gems)
    while True:
        if len(numOfGem) < numOfKind:
            r += 1
            if r >= lenOfDis:
                break
            gem = gems[r]
            if gem not in numOfGem:
                numOfGem[gem] = 1
            else:
                numOfGem[gem] += 1
        else: # len(numOfGem) = numOfKind
            if l >= lenOfDis:
                break
            ans.append( (l, r) )
            gem = gems[l]
            numOfGem[gem] -= 1
            if numOfGem[gem] == 0:
                del numOfGem[gem]
            l += 1
    ans = sorted(ans, key=lambda x : (x[1]-x[0], x[0]))
    a, b = ans[0]
    return( [a+1, b+1] )

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(['A']))
print(solution(["A","A","A","B","B"]))
print(solution(["A","B","B","B","B","B","B","C","B","A"]))