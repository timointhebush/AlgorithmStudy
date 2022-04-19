import sys

input = sys.stdin.readline


def mul(A: list, C: list) -> list:
    N = len(A)
    result = [[0 for _ in range(N)] for _ in range(N)]
    for row in range(N):
        for col in range(N):
            value = 0
            for idx in range(N):
                value += A[row][idx] * C[idx][col]
            result[row][col] = value % 1000
    return result


def power_of(A: list, B: int) -> list:
    if B == 1:
        return A

    tmp = power_of(A, B // 2)
    if B % 2 == 0:
        return mul(tmp, tmp)
    else:
        return mul(mul(tmp, tmp), A)


if __name__ == "__main__":
    N, B = tuple(map(int, input().split()))
    A = []
    for _ in range(N):
        row = list(map(int, input().split()))
        A.append(row)
    answer = power_of(A, B)
    for row in answer:
        for col in row:
            print(col % 1000, end=" ")
        print()
