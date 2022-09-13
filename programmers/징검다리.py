def solution(stones, k):
    min_cross, max_cross = 1, max(stones)
    while min_cross < max_cross:
        tmp_cross = (min_cross + max_cross) // 2

        no_stone = 0
        for stone_num in stones:
            if (stone_num - tmp_cross) <= 0:
                no_stone += 1
                if no_stone >= k:
                    break
            else:
                no_stone = 0

        if no_stone >= k:
            max_cross = tmp_cross
        else:
            min_cross = tmp_cross + 1

    return max_cross


if __name__ == "__main__":
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))