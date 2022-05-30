from collections import deque

tmp = input().split(" ")
N, Q = int(tmp[0]), int(tmp[1])
tree = [{} for i in range(N+1)] #영상 번호와 index를 동일하게 하기 위해 N+1개

for i in range(N-1):
    tmp = input().split(" ")
    p, q, r = int(tmp[0]), int(tmp[1]), int(tmp[2])
    tree[p][q] = r
    tree[q][p] = r

questions = []
for i in range(Q):
    tmp = input().split(" ")
    K, V = int(tmp[0]), int(tmp[1])
    questions.append((K, V))

for K, V in questions:
    ans = 0
    visited = [False for i in range(N+1)]
    queue = deque()
    queue.append((V, float('inf')))
    visited[V] = True
    while len(queue) != 0:
        v, min_r = queue.popleft()
        for connected, r in tree[v].items():
            if visited[connected] == True:
                pass
            else:
                visited[connected] = True
                if r < min_r:
                    if r >= K:
                        ans += 1
                    queue.append((connected, r))
                else:
                    if min_r >= K:
                        ans += 1
                    queue.append((connected, min_r))
    print(ans)