from collections import deque
from copy import deepcopy


def solution(storey):
    str_list_storey = list(map(int, str(storey)))
    str_len = len(str_list_storey)
    answer = float("inf")

    q = deque()
    q.append([str_list_storey, str_len - 1, 0])
    while q:
        tmp_list, cur_idx, cur_btn_cnt = q.popleft()
        if cur_idx == -1:
            answer = min(answer, cur_btn_cnt)
            continue
        for standard in [0, 10]:
            if standard == 10:
                differ = standard - tmp_list[cur_idx]

                copy_list = deepcopy(tmp_list)
                copy_list = list(map(str, copy_list))
                copy_num = int("".join(copy_list))
                copy_num += 10**(str_len - cur_idx)
                copy_list = list(map(int, str(copy_num)))
                copy_list[cur_idx] = 0

                q.append([copy_list, cur_idx - 1, cur_btn_cnt + differ])
            else: # standard == 0
                differ = tmp_list[cur_idx] - standard

                copy_list = deepcopy(tmp_list)
                copy_list[cur_idx] = 0

                # copy_list = list(map(str, copy_list))
                # copy_num = int("".join(copy_list))
                # copy_num -= 10 ** (str_len - 1 - cur_idx)
                # copy_list = list(map(int, str(copy_num)))

                q.append([copy_list, cur_idx - 1, cur_btn_cnt + differ])
    return answer


if __name__ == "__main__":
    print(solution(2554))