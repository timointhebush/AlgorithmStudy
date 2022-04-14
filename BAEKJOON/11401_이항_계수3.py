import sys
input = sys.stdin.readline

def power(a, b):
    if b == 0:
        return 1
    if b % 2 == 0: # 짝수
        return (power(a, b//2) ** 2) % P
    else: # 홀수
        return (power(a, b//2) ** 2) * a % P

P = 1000000007

N, K = tuple(map(int, input().split()))

fact = [1 for _ in range(N + 1)]
for i in range(2, N + 1):
    fact[i] = (fact[i - 1] * i) % P

top = fact[N]
bottom = (fact[N - K] * fact[K]) % P

print((top * power(bottom, P - 2)) % P)
