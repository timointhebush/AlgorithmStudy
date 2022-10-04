from collections import defaultdict, deque
import copy


def solution(gems):
    gem_to_num = defaultdict(int)
    for gem in gems:
        gem_to_num[gem] += 1
    left, right = 0, len(gems) - 1
    q = deque()
    q.append((left, right, copy.deepcopy(gem_to_num)))

    while q:
        cur_l, cur_r, cur_num = q.popleft()
        if cur_l >= cur_r:
            continue

        gem = gems[cur_l]
        if cur_num[gem] > 1:
            nxt_l = cur_l + 1
            length = cur_r - nxt_l
            min_length = right - left
            if length < min_length or (length == min_length and cur_l < left):
                left, right = nxt_l, cur_r
            if cur_num[gem] > 1:
                cur_num[gem] -= 1
                q.append((nxt_l, cur_r, copy.deepcopy(cur_num)))
                cur_num[gem] += 1

        gem = gems[cur_r]
        if cur_num[gem] > 1:
            nxt_r = cur_r - 1
            length = nxt_r - cur_l
            min_length = right - left
            if length < min_length or (length == min_length and cur_l < left):
                left, right = cur_l, nxt_r
            if cur_num[gem] > 1:
                cur_num[gem] -= 1
                q.append((cur_l, nxt_r, copy.deepcopy(cur_num)))
                cur_num[gem] += 1
    return [left + 1, right + 1]


if __name__ == "__main__":
    print(solution(["AA", "AB", "AC", "AA", "AC"]))
    print(solution(["XYZ", "XYZ", "XYZ"]))
    print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))