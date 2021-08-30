class Staff:
    def __init__(self, id, sales):
        self.id = id
        self.sales = sales
        self.team = {"leader": self}


class Tree:
    def __init__(self, ceo_sales):
        self.ceo = Staff(1, ceo_sales)


def solution(sales, links):
    answer = 0
    tree = Tree(sales[0])

    team = {}
    links = sorted(links, key=lambda x: (x[0], x[1]))
    for link in links:
        leader_id, staff_id = link
        if leader_id not in team:
            team[leader_id] = {leader_id: sales[leader_id - 1], staff_id: sales[staff_id - 1]}
        else:
            team[leader_id][staff_id] = sales[staff_id - 1]

    return answer
