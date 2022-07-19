def solve():
    for command in command_list:
        if len(command) > 3:
            command, x = command.split(" ")
            x = int(x)
        func = command_to_func[command]
        if command == "NUM":
            func(x)
        else:
            func()
        if is_error:
            print("ERROR")
            return

    if is_error or len(stack) != 1:
        print("ERROR")
    else:
        print(stack[-1])


def num(x):
    stack.append(x)


def pop():
    global is_error
    if len(stack) < 1:
        is_error = True
        return
    stack.pop()


def inv():
    global is_error
    if len(stack) < 1:
        is_error = True
        return
    stack[-1] = -stack[-1]


def dup():
    global is_error
    if len(stack) < 1:
        is_error = True
        return
    stack.append(stack[-1])


def swp():
    global is_error
    if len(stack) < 2:
        is_error = True
        return
    first = stack.pop()
    second = stack.pop()
    stack.append(first)
    stack.append(second)


def add():
    global is_error
    if len(stack) < 2:
        is_error = True
        return
    first = stack.pop()
    second = stack.pop()
    val = first + second
    if abs(val) >= 10 ** 9:
        is_error = True
        return
    stack.append(val)


def sub():
    global is_error
    if len(stack) < 2:
        is_error = True
        return
    first = stack.pop()
    second = stack.pop()
    val = second - first
    if abs(val) >= 10 ** 9:
        is_error = True
        return
    stack.append(val)


def mul():
    global is_error
    if len(stack) < 2:
        is_error = True
        return
    first = stack.pop()
    second = stack.pop()
    val = second * first
    if abs(val) >= 10 ** 9:
        is_error = True
        return
    stack.append(val)


def div():
    global is_error
    if len(stack) < 2:
        is_error = True
        return
    first = stack.pop()
    second = stack.pop()
    if first == 0:
        is_error = True
        return
    val = abs(second) // abs(first)
    if first * second < 0:
        val *= -1
    stack.append(val)


def mod():
    global is_error
    if len(stack) < 2:
        is_error = True
        return
    first = stack.pop()
    second = stack.pop()
    if first == 0:
        is_error = True
        return
    val = abs(second) % abs(first)
    if second < 0:
        val *= -1
    stack.append(val)


if __name__ == "__main__":
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
    is_quit = False
    while True:
        is_error = False
        command_list = []
        while True:
            command = input()
            if command == "END":
                break
            if command == "QUIT":
                is_quit = True
                break
            command_list.append(command)

        if is_quit:
            break

        stack = []
        N = int(input())
        for i in range(N):
            stack = [int(input())]
            solve()
        input()
        print()
