from collections import defaultdict


def solution(fees, records):
    default_time, default_fee, unit_time, unit_fee = fees[0], fees[1], fees[2], fees[3]
    db = {}
    db["IN"] = defaultdict(list)
    db["OUT"] = defaultdict(list)
    nums = set()
    for record in records:
        time, num, dir = record.split(" ")
        minute = parse_to_min(time)
        db[dir][num].append(minute)
        nums.add(num)

    answer = []
    nums = sorted(list(nums), key=lambda x: int(x))
    for num in nums:
        in_mins = db["IN"][num]
        out_mins = db["OUT"][num]
        tmp_total_min = 0
        for i in range(min(len(in_mins), len(out_mins))):
            tmp_total_min += out_mins[i] - in_mins[i]
        if len(in_mins) > len(out_mins):
            tmp_total_min += (23 * 60 + 59) - in_mins[len(in_mins) - 1]

        if tmp_total_min > default_time:
            extra_min = tmp_total_min - default_time
            unit = extra_min // unit_time
            if extra_min % unit_time != 0:
                unit += 1
            answer.append(unit_fee * unit + default_fee)
        else:
            answer.append(default_fee)
    return answer


def parse_to_min(time):
    hour, minute = map(int, time.split(":"))
    return 60 * hour + minute


if __name__ == "__main__":
    print(solution([180, 5000, 10, 600],
                   ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
                    "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
