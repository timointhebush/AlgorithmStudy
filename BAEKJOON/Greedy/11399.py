N = int(input())
P = [int(i) for i in input().split(" ")]
P.sort()
for i in range(1, N):
    P[i] = P[i-1] + P[i]
print(sum(P))