from collections import defaultdict, deque
from copy import deepcopy


def create_tickets_set(tickets):
    tickets_set = defaultdict(int)
    for depart, arrive in tickets:
        tickets_set[(depart, arrive)] += 1
    return tickets_set


def create_graph(tickets):
    graph = defaultdict(set)
    for depart, arrive in tickets:
        graph[depart].add(arrive)
    return graph


def is_end(tickets_set: dict):
    for num in tickets_set.values():
        if num > 0:
            return False
    return True


def solution(tickets):
    graph = create_graph(tickets)
    tickets_set = create_tickets_set(tickets)
    route = ["ICN"]
    q = deque([(route, tickets_set)])

    route_candidate_list = []

    while q:
        cur_route, cur_tickets_set = q.popleft()
        if is_end(cur_tickets_set):
            route_candidate_list.append(cur_route)
        cur_airport = cur_route[-1]
        can_arrive_airport_set = graph[cur_airport]
        for can_arrive_airport in can_arrive_airport_set:
            if cur_tickets_set[(cur_airport, can_arrive_airport)] > 0:
                nxt_route = deepcopy(cur_route)
                nxt_visited = deepcopy(cur_tickets_set)
                nxt_route.append(can_arrive_airport)
                nxt_visited[(cur_airport, can_arrive_airport)] -= 1
                q.append((nxt_route, nxt_visited))
    route_candidate_list.sort()
    return route_candidate_list[0]


if __name__ == "__main__":
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
