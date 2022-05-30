def search(C, lo, hi, n):
    if lo == hi:
        return lo
    elif lo + 1 == hi: 
        if C[lo] >= n:
            return lo
        else: #C[lo] < n
            return hi
    mid = (lo + hi) // 2
    if C[mid] == n:
        return mid
    elif C[mid] > n:
        return search(C, lo, mid, n)
    else: #C[mid] < n
        return search(C, mid+1, hi, n)

N = int(input())
connect_info = []
for i in range(N):
    tmp = input().split(" ")
    connect_info.append(    (  int(tmp[0]), int(tmp[1])  )     )
connect_info = sorted(connect_info, key = lambda x : x[0])

C = [float("inf") for i in range(N+1)]
C[0] = float("-inf")
C[1] = connect_info[0][1]
longest_idx = 1

for idx, n in connect_info:
    if C[longest_idx] < n:
        longest_idx += 1
        C[longest_idx] = n
    else:
        # i는 C[i-1] < n <= C[i]를 만족한다. 즉 
        i = search(C, 0, longest_idx, n)
        C[i] = n

print(N - longest_idx)
