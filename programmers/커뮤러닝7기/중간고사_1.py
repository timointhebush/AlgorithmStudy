from collections import deque


def solution(booked, unbooked):
    booked_q = deque(convert_to_minute(booked))
    unbooked_q = deque(convert_to_minute(unbooked))
    current_minute = min(booked_q[0][0], unbooked_q[0][0])
    answer = []
    target_q = booked_q
    while booked_q or unbooked_q:
        can_work = False
        if not can_work and len(booked_q) > 0:
            if booked_q[0][0] <= current_minute:
                target_q = booked_q
                can_work = True
        if not can_work and len(unbooked_q) > 0:
            if unbooked_q[0][0] <= current_minute:
                target_q = unbooked_q
                can_work = True
        if can_work:
            customer_arrive, customer_name = target_q.popleft()
            answer.append(customer_name)
            current_minute = customer_arrive + 10
        else:
            if booked_q and unbooked_q:
                current_minute = min(booked_q[0][0], unbooked_q[0][0])
            elif booked_q and not unbooked_q:
                current_minute = booked_q[0][0]
            else:
                current_minute = unbooked_q[0][0]
    return answer


def convert_to_minute(customer_list: list) -> list:
    converted_list = []
    str_time: str
    name: str
    for str_time, name in customer_list:
        hour, minute = map(int, str_time.split(":"))
        minute += 60 * hour
        converted_list.append([minute, name])
    return converted_list


if __name__ == "__main__":
    # print(solution([["09:10", "lee"]], [["09:00", "kim"], ["09:05", "bae"]]))
    # print(solution([["09:55", "hae"], ["10:05", "jee"]], [["10:04", "hee"], ["14:07", "eom"]]))
    print(solution([["00:01", "bookA"]], [["00:02", "unA"], ["00:03", "unB"]]))
