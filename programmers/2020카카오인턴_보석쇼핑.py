from collections import defaultdict


def solution(gems):
    left, right = 0, 0
    num_of_types = len(set(gems))
    gem_to_num = defaultdict(int)
    gem_to_num[gems[0]] = 1
    last_idx = len(gems) - 1
    answer = []
    while True:
        current_num_of_types = len(gem_to_num)
        if current_num_of_types < num_of_types:
            right += 1
            if right > last_idx:
                break
            gem = gems[right]
            gem_to_num[gem] += 1
        else:  # len(gem_to_num) == num_of_types
            if left > last_idx:
                break
            answer.append((left, right))

            gem = gems[left]
            gem_to_num[gem] -= 1
            if gem_to_num[gem] == 0:
                del gem_to_num[gem]
            left += 1

    answer = sorted(answer, key=lambda x: (x[1] - x[0], x[0]))
    a, b = answer[0]
    return [a + 1, b + 1]


if __name__ == "__main__":
    print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))