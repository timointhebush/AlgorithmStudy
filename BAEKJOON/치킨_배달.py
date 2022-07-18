from itertools import combinations

N, M = tuple(map(int, input().split(" ")))
board = []
house_list = []
chicken_list = []
for r in range(N):
    row = input().split(" ")
    for c in range(N):
        if row[c] == '1':
            house_list.append((r, c))
        elif row[c] == '2':
            chicken_list.append((r, c))


def get_chicken_length(house, chicken_idxes):
    chicken_length = float("inf")
    for chicken_idx in chicken_idxes:
        chicken = chicken_list[chicken_idx]
        length = get_length(house, chicken)
        chicken_length = min(chicken_length, length)
    return chicken_length


def get_length(house, chicken):
    r1, c1 = house
    r2, c2 = chicken
    return abs(r1 - r2) + abs(c1 - c2)


answer = float("inf")
chicken_list_comb = combinations(range(len(chicken_list)), M)
for chicken_idxes in chicken_list_comb:
    tmp = 0
    for house in house_list:
        tmp += get_chicken_length(house, chicken_idxes)
    answer = min(answer, tmp)

print(answer)


