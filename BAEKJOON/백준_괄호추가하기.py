from itertools import combinations


def solution():
    N = int(input())
    formula = input()
    ans_cand = []
    if N <= 3:
        return calculate(formula)
    n_op = N // 2
    n_num = N - n_op
    n_brack_pair = n_num // 2
    brack_cases_formulas = get_brack_cases_formula(formula, n_op, n_brack_pair)
    for case_formula in brack_cases_formulas:
        ans_cand.append(calculate(case_formula))
    return max(ans_cand)


def get_brack_cases_formula(formula, n_op, n_brack_pair):
    brack_op_cand_idxes = []
    for n_brack_pair_cand in range(1, n_brack_pair + 1):
        tmp = combinations(range(n_op), n_brack_pair_cand)
        brack_op_cand_idxes += list(tmp)
    del_continue_brack_idx_case(brack_op_cand_idxes)
    formula_cand = []
    for idx_case in brack_op_cand_idxes:
        formula_cand.append(make_idx_brack_formula(formula, idx_case))
    return formula_cand


def del_continue_brack_idx_case(brack_op_cand_idxes):
    del_idx_list = []
    for i_case, idxes_case in enumerate(brack_op_cand_idxes):
        n = len(idxes_case)
        for i in range(n - 1):
            j = i + 1
            if idxes_case[j] == idxes_case[i] + 1:
                del_idx_list.append(i_case)
                break
    if len(del_idx_list) >= 1:
        for i in del_idx_list[::-1]:
            del brack_op_cand_idxes[i]


def make_idx_brack_formula(formula, idx_case):
    formula = list(formula)
    for i in list(idx_case)[::-1]:
        formula.insert(i * 2 + 3, ")")
        formula.insert(i * 2, "(")
    return "".join(formula)


def calculate(formula):
    post_formula_list = make_post_formula(formula)
    stack = []
    for X in post_formula_list:
        if X in ["+", "-", "*"]:
            B = stack.pop()
            A = stack.pop()
            stack.append(cal(A, B, X))
        else:
            stack.append(X)
    return int(stack.pop())


def cal(A, B, X):
    if X == "+":
        return A + B
    elif X == "-":
        return A - B
    else:
        return A * B


def make_post_formula(formula):
    formula = list(formula)
    post_formula = []
    stack = []
    brack = False
    for X in formula:
        if X in ["+", "-", "*"]:
            while len(stack) != 0 and stack[-1] in ["+", "-", "*"]:
                post_formula.append(stack.pop())
            stack.append(X)
        elif X == "(":
            brack = True
            stack.append(X)
        elif brack == True and X == ")":
            brack = False
            while stack[-1] != "(":
                post_formula.append(stack.pop())
            stack.pop()
        else:
            post_formula.append(int(X))
    while len(stack) != 0:
        post_formula.append(stack.pop())
    return post_formula


print(solution())
