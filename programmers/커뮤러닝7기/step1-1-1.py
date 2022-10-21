RED = 1
GREEN = 2


def solution(bell):
    for i in range(len(bell)):
        if bell[i] == RED:
            bell[i] = -1
        else:
            bell[i] = 1

    new_bell = [0 for _ in range(len(bell))]
    new_bell[0] = bell[0]

    for i in range(1, len(bell)):
        new_bell[i] = new_bell[i - 1] + bell[i]

    min_idx, max_idx = 0, 0
    for i in range(len(bell)):
        if new_bell[i] == 0:
            min_idx = min(min_idx, i)
            max_idx = max(max_idx, i)

    return max_idx - min_idx


if __name__ == "__main__":
    print(solution([1, 2, 1, 1, 1, 2, 2, 1]))