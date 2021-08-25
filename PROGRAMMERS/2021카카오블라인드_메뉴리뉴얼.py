def solution(orders, course):
    answer = []
    orders = sorted(orders, key=lambda x: (len(x), x))
    cand = {}
    new_orders = []
    for i, order in enumerate(orders):
        if tuple(set(order)) in cand:
            cand[tuple(set(order))] += 1
        else:
            cand[tuple(set(order))] = 1
            new_orders.append(order)

    n = len(new_orders)

    for a in range(n):
        for b in range(a+1, n):
            interSec = tuple(set( new_orders[a] ) & set( new_orders[b] ))
            if len(interSec) >= 2:
                if interSec not in cand:
                    cand[interSec] = 1
                else:
                    cand[interSec] += 1

    keys = list(cand.keys())
    keys = sorted(keys, key=lambda x : len(x))
    # for a in range(len(keys))
    #     for 


    print(keys)

    return answer

print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
# print(solution(['AB', 'CD','CD','CD','CD','CDE' ], [1, 2, 3]))