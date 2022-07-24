import sys


def solve():
    global N, K, learned_chars, word_set_list
    N, K = map(int, input().split())
    if K < 5:
        return 0
    elif K == 26:
        return N

    learned_chars = {'a', 'n', 't', 'i', 'c'}
    word_set_list = [set() for _ in range(N)]

    for i in range(N):
        word_set = set(input())
        word_set_list[i] = word_set
    dfs(5, ord('a'))
    return answer


def dfs(learned_cnt: int, prev_idx: int):
    global answer, learned_chars
    if learned_cnt >= K:
        tmp_answer = 0
        for word_set in word_set_list:
            can_read = True
            for char in word_set:
                if char not in learned_chars:
                    can_read = False
                    break
            if can_read:
                tmp_answer += 1
        answer = max(answer, tmp_answer)
    else:
        for idx in range(prev_idx, ord('z') + 1):
            char = chr(idx)
            if char not in learned_chars:
                learned_chars.add(char)
                dfs(learned_cnt + 1, idx)
                learned_chars.remove(char)


if __name__ == "__main__":
    sys.stdin = open("가르침.txt", "r")
    N, K = 0, 0
    learned_chars = set()
    word_set_list = []
    answer = 0
    print(solve())
