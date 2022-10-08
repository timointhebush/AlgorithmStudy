from collections import defaultdict


def solution(n, k, cmd):
    # chart = [i for i in range(n)]
    deleted_idx_stack = []
    is_deleted = defaultdict(bool)
    for command in cmd:
        command = command.split(" ")
        if command[0] == "U" or command[0] == "D":
            X = int(command[1])
            dir = -1 if command[0] == "U" else 1
            while X > 0:
                k += dir
                if not is_deleted[k]:
                    X -= 1
        elif command[0] == "C":
            deleted_idx_stack.append(k)
            is_deleted[k] = True
            dir = -1 if k == n - 1 else 1
            while True:
                tmp_k = k + dir
                if tmp_k < 0 or tmp_k >= n:
                    break
                k = tmp_k
                if not is_deleted[k]:
                    break
        else:  # "Z"
            idx = deleted_idx_stack.pop()
            is_deleted[idx] = False

    answer = ''
    for i in range(n):
        if is_deleted[i]:
            answer += 'X'
        else:
            answer += 'O'
    return answer


if __name__ == "__main__":
    # print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
    print(solution(5, 0, ["D 3", "C", "U 3", "C", "D 2", "C"]))
