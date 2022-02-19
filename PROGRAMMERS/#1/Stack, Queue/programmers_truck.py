def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    while truck_weights or bridge:
        answer += 1
        if truck_weights:
            if sum(list(map(lambda x: x[0], bridge))) + truck_weights[0]<= weight:
                bridge.append((truck_weights.pop(0), answer + bridge_length - 1))

        del_list = []
        for idx, truck in enumerate(bridge):
            if truck[1] == answer:
                del_list.append(idx)
        while del_list:
            del bridge[del_list.pop()]
    return answer + 1

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]))