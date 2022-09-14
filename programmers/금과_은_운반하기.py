def solution(a, b, g, s, w, t):
    min_time = 0
    max_time = 10 ** 5 * 10 ** 9 * 4
    answer = 10 ** 5 * 10 ** 9 * 4
    num_of_cities = len(g)
    total = a + b
    while min_time <= max_time:
        tmp_time = (min_time + max_time) // 2
        tmp_a, tmp_b = 0, 0
        tmp_total = 0
        for i in range(num_of_cities):
            g_i, s_i = g[i], s[i]
            w_i, t_i = w[i], t[i]
            move_i = tmp_time // (t_i * 2)
            if tmp_time % (t_i * 2) >= t_i:
                move_i += 1

            tmp_a += g_i if w_i * move_i >= g_i else w_i * move_i
            tmp_b += s_i if w_i * move_i >= s_i else w_i * move_i
            tmp_total += g_i + s_i if w_i * move_i >= g_i + s_i else w_i * move_i

        if tmp_a >= a and tmp_b >= b and tmp_total >= total:
            max_time = tmp_time - 1
            answer = min(answer, tmp_time)
        else:
            min_time = tmp_time + 1
    return answer


if __name__ == "__main__":
    print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))
