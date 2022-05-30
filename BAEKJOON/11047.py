tmp = input().split(" ")
N = int(tmp[0])
K = int(tmp[1])
coins = []
for i in range(N):
    coins.append(int(input()))
answer = 0
for i in range(N-1, -1, -1):
    num = K // coins[i]
    answer += num
    K = K - num*coins[i]
    if K == 0:
        break
print(answer)