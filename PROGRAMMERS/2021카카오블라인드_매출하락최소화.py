def solution(sales, links):
    global tree, d, sales_
    sales_ = sales
    tree = make_tree(links)
    d = [[-1, -1] for _ in range(len(sales) + 1)]
    return min(get_min_sales(1, 1), get_min_sales(1, 0))


def make_tree(links):
    tree = {}
    for i in range(len(sales_)):
        tree[i + 1] = []
    for link in links:
        tree[link[0]].append(link[1])
    return tree


def get_min_sales(i, root):
    if d[i][root] != -1:
        return d[i][root]
    child_sum = 0
    if root == 1:
        for child in tree[i]:
            child_sum += min(get_min_sales(child, 1), get_min_sales(child, 0))
        d[i][root] = child_sum + sales_[i - 1]
        return d[i][root]
    else:
        flag = False
        # 이부분 실수있었음. 팀원이 아무도 없는 경우를 고려하지 않음.
        diff = 0 if len(tree[i]) == 0 else float("inf")
        for child in tree[i]:
            if get_min_sales(child, 0) > get_min_sales(child, 1):
                flag = True
            else:
                diff = min(diff, get_min_sales(child, 1) - get_min_sales(child, 0))
            child_sum += min(get_min_sales(child, 1), get_min_sales(child, 0))
        d[i][root] = child_sum
        if flag == False:
            d[i][root] += diff
        return d[i][root]


print(
    solution(
        [14, 17, 15, 18, 19, 14, 13, 16, 28, 17],
        [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]],
    )
)
