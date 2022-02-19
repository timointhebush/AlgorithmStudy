def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    bridge_sum = 0
    while truck_weights:
        answer += 1
        bridge_sum -= bridge.pop(0)
        if bridge_sum + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            bridge.append(truck)
            bridge_sum += truck
        else:
            bridge.append(0)
    while bridge:
        answer += 1
        bridge.pop()
    return answer

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]))