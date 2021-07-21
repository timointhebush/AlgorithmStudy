def solution(gems):
    answer = []
    gemSet = set(gems)
    gemN = len(gemSet)
    N = len(gems)
    for rng in range(gemN, N+1):
        for start in range(N-rng+1):
            copyOfGemSet = gemSet.copy()
            for idx in range(start, start+rng):
                if gems[idx] in copyOfGemSet:
                    copyOfGemSet.remove(gems[idx])
            if len(copyOfGemSet) == 0:
                return [start+1, start+rng]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print()