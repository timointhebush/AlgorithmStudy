def solution(n, lost, reserve):
    lost_set, reserve_set = set(lost), set(reserve)

    reserve = reserve_set - lost_set
    lost = lost_set - reserve_set
    answer = n

    for i in lost:
        if i - 1 in reserve:
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            reserve.remove(i + 1)
        else:
            answer -= 1
    return answer


if __name__ == "__main__":
    print(solution(3, [3], [1]))