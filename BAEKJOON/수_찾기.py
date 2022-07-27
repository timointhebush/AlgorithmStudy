if __name__ == "__main__":
    N = int(input())
    nums = set(map(int, input().split()))
    M = int(input())
    target_nums = list(map(int, input().split()))
    for num in target_nums:
        if num in nums:
            print(1)
        else:
            print(0)