def solution(name):
    name = list(name)
    n = len(name)
    A_name = ['A' for i in range(n)]
    idx = 0
    answer = 0
    while True:
        move = getAlphabetMove(A_name[idx], name[idx])
        A_name[idx] = name[idx]
        answer += move
        
        nextIdxMove = getNextIdxMove(idx, n, A_name, name)
        if nextIdxMove==None:
            break
        idx = nextIdxMove[0]
        answer += nextIdxMove[1]

    return answer

def getAlphabetMove(current, target):
    move = ord(target) - ord(current)
    if move > 13:
        move = 26-move
    return move

def getNextIdxMove(current, n, A_name, name):
    for move in range(1, int(n/2)+1):
        right = (current+move)%n
        left = (current-move)%n
        if A_name[right] != name[right]:
            return [right, move]
        elif A_name[left] != name[left]:
            return [left, move]
    return None

print(solution("JAN"))