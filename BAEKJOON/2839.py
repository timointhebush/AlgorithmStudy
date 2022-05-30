N = int(input())
max_num5 = N // 5
status = False
for num5 in range(max_num5, -1, -1):
    tmp_N = N
    ans = 0
    ans += num5
    tmp_N -= 5*num5
    num3 = tmp_N // 3
    ans += num3
    tmp_N -= 3*num3
    if tmp_N == 0:
        status = True
        break
if status == True:
    print(ans)
else:
    print(-1)