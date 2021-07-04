N = int(input())
meetings = []
for i in range(N):
    tmp = input().split(" ")
    meetings.append((int(tmp[0]), int(tmp[1])))

meetings = sorted(meetings, key=lambda meeting: (meeting[1], meeting[0]))

meeting_progress = meetings.pop(0)
ans = 1
for start, end in meetings:
    if meeting_progress[1] <= start:
        meeting_progress = (start, end)
        ans += 1
print(ans)