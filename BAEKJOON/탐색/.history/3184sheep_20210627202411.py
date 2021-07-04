# 울타리의 사이즈를 입력받는다.
size = input().split(" ")
row_size, col_size = int(size[0]), int(size[1])
# 입력받은 사이즈를 바탕으로 뒷마당 데이터를 입력받는다.
backyard = []
for i in range(row_size):
    backyard.append(input().split(" "))
