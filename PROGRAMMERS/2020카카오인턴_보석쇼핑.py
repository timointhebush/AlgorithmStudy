def solution(gems):
    ans = []
    n = len(gems)
    numOfTypes = len(set(gems))
    l, r = 0, 0
    numOfGems = {gems[l] : 1}
    while l < n and r < n:
        if len(numOfGems) < numOfTypes:
            if r+1 <n:
                r += 1
                gem  = gems[r]
                if gem in numOfGems:
                    numOfGems[gem] += 1
                else:
                    numOfGems[gem] = 1
        else: # len(numOfGems) = numOfTypes
            ans.append((l, r))
            gem = gems[l]
            numOfGems[gem] -= 1
            if numOfGems[gem] == 0:
                del numOfGems[gem]
            l += 1
            
    return(ans)

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(['A']))
print(solution(["A","A","A","B","B"]))
print(solution(["A","B","B","B","B","B","B","C","B","A"]))