def solution(k, room_number):
    answer = []
    hotel = {}
    for customerWants in room_number:
        roomN = customerWants
        tmp = []
        while True:
            if roomN in hotel:
                tmp.append(roomN)
                roomN = hotel[roomN] + 1
            else:
                hotel[roomN] = roomN
                answer.append(roomN)
                for i in tmp:
                    hotel[i] = roomN
                break
    return answer

print(solution(10, [1,3,4,1,3,1]))