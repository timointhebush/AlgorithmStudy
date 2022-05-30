def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers = sorted(str_numbers, reverse=True, key=lambda x: x*3)
    return str(int(''.join(str_numbers)))

def solution2(numbers):
    str_numbers = list(map(str, numbers))
    quickSort(str_numbers, 0, len(str_numbers)-1)
    return str(int(''.join(str_numbers)))

def quickSort(data, first_idx, last_idx):
    if first_idx <= last_idx:
        mid_idx = partition(data, first_idx, last_idx)
        quickSort(data, first_idx, mid_idx-1)
        quickSort(data, mid_idx+1, last_idx)

def partition(data, first_idx, last_idx):
    if first_idx <= last_idx:
        pivot = data[last_idx]
        insert_idx = first_idx
        for compare_idx in range(first_idx, last_idx+1):
            if compare(pivot, data[compare_idx]) < 0:
                data[insert_idx], data[compare_idx] = data[compare_idx], data[insert_idx]
                insert_idx += 1
        data[insert_idx], data[last_idx] = data[last_idx], data[insert_idx]
        return insert_idx

def compare(a, b):
    '''
    a와 b는 str, ab-ba > 0이라면, 문제 기준에 의해 a>b이다.
    '''
    return int(a + b) - int(b + a)

print(solution([3, 30, 34, 5, 9]))
print(solution2([3, 30, 34, 5, 9]))