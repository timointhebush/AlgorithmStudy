import sys

if __name__ == "__main__":
    sys.stdin = open("후보_추천하기.txt", "r")

    N = int(input())
    total_likes = int(input())
    like_seq = list(map(int, input().split()))

    pictures = {}

    for seq, student in enumerate(like_seq):
        if student not in pictures:
            if len(pictures) >= N:
                sorted_pictures = sorted(pictures.items(), key=lambda x: x[1])
                # print(sorted_pictures)
                del_student = sorted_pictures[0][0]
                del pictures[del_student]
            pictures[student] = 1
        else:
            like = pictures[student]
            pictures[student] = like + 1

    answer = list(map(str, sorted(pictures.keys())))
    print(" ".join(answer))

