import sys

def solve():
    try:
        for command in command_list:
            command = command.split()
            func = command_to_func[command[0]]
            if len(command) > 1:
                func(int(command[1]))
            else:
                func()
        if len(stack) != 1:
            raise IndexError
        print(stack[-1])
    except (ValueError, IndexError, ZeroDivisionError):
        print("ERROR")


def num(x):
    stack.append(x)


def pop():
    stack.pop()


def inv():
    val = stack.pop()
    stack.append(-1 * val)


def dup():
    val = stack.pop()
    stack.append(val)
    stack.append(val)


def swp():
    first = stack.pop()
    second = stack.pop()
    stack.append(first)
    stack.append(second)


def add():
    first = stack.pop()
    second = stack.pop()
    val = first + second
    check_val(val)
    stack.append(val)


def sub():
    first = stack.pop()
    second = stack.pop()
    val = second - first
    check_val(val)
    stack.append(val)


def mul():
    first = stack.pop()
    second = stack.pop()
    val = second * first
    check_val(val)
    stack.append(val)


def div():
    first = stack.pop()
    second = stack.pop()
    val = abs(second) // abs(first)
    if first * second < 0:
        val *= -1
    check_val(val)
    stack.append(val)


def mod():
    first = stack.pop()
    second = stack.pop()
    val = abs(second) % abs(first)
    if second < 0:
        val *= -1
    check_val(val)
    stack.append(val)


def until_quit():
    global command_list, stack
    while True:
        command_list = []
        while True:
            command = input()
            if command == "QUIT":
                return 0
            elif command != "END":
                command_list.append(command)
            else:
                break

        N = int(input())
        for _ in range(N):
            stack = [int(input())]
            solve()
        empty = input()
        print(empty)


def check_val(val):
    if abs(val) > 10 ** 9:
        raise ValueError


if __name__ == "__main__":
    sys.stdin = open("고스택.txt", "r")

    command_to_func = {
        "NUM": num,
        "POP": pop,
        "INV": inv,
        "DUP": dup,
        "SWP": swp,
        "ADD": add,
        "SUB": sub,
        "MUL": mul,
        "DIV": div,
        "MOD": mod
    }

    command_list = []
    stack = []
    until_quit()
