from collections import defaultdict

name_to_income = defaultdict(int)
enroll_list = []
referral_list = []
enroll_idx = {}


def solution(enroll, referral, seller, amount):
    global enroll_list, referral_list, enroll_idx
    enroll_list = enroll
    referral_list =referral
    for i, name in enumerate(enroll):
        enroll_idx[name] = i
    for i, name in enumerate(seller):
        sell_income = amount[i] * 100
        cal_comm(name, sell_income)
    answer = [name_to_income[name] for name in enroll]
    return answer


def cal_comm(name, income):
    global name_to_income
    comm = int(income * 0.1)
    name_to_income[name] += income - comm
    if comm != 0 and name in enroll_idx:
        idx = enroll_idx[name]
        boss_name = referral_list[idx]
        cal_comm(boss_name, comm)


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))