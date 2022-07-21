from itertools import combinations


N, M = tuple(map(int, input().split(" ")))
nums = list(map(int, input().split(" ")))
accum = [0 for _ in range(len(nums) + 1)]

for i in range(1, len(nums) + 1):
    accum[i] = accum[i - 1] + nums[i - 1]

print("accum ", accum)

answer = 0
for a, b in combinations(range(len(nums) + 1), 2):
    right = max(a, b)
    left = min(a, b)
    if accum[right] - accum[left] == M:
        answer += 1

print(answer)