def getDist(a, b, keypad):
    change = {"*":10, 0:11, "#":12}
    if a=='*' or a==0 or a=='#':
        a = change[a]
    if b=='*' or b==0 or b=='#':
        b = change[b]
    row1, col1 = keypad[a]
    row2, col2 = keypad[b]
    return sum( (abs(row1 - row2), abs(col1 - col2)) )

def solution(numbers, hand):
    answer = ''
    l, r = '*', '#'
    keypad_dist = {
        1 : (0, 0), 2 : (0, 1), 3 : (0, 2),
        4 : (1, 0), 5 : (1, 1), 6 : (1, 2),
        7 : (2, 0), 8 : (2, 1), 9 : (2, 2),
        10 : (3, 0), 11 : (3, 1), 12 : (3, 2) 
    }
    keypad = {
        1 : 'l', 2 : 'm', 3 : 'r',
        4 : 'l', 5 : 'm', 6 : 'r',
        7 : 'l', 8 : 'm', 9 : 'r',
         0 : 'm'
    }
    for n in numbers:
        left = True
        if keypad[n] == 'm':
            l_dist, r_dist = getDist(n, l, keypad_dist), getDist(n, r, keypad_dist)
            if l_dist < r_dist:
                pass
            elif l_dist > r_dist:
                left = False
            else:
                if hand == 'right':
                    left = False
        else:
            if keypad[n] == 'r':
                left = False
        if left:
            answer += "L"
            l = n
        else:
            answer += "R"
            r = n
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print("LRLLLRLLRRL")
print("")

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print("LRLLRRLLLRR")