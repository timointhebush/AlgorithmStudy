a = [123, [1, 2]]
b = a.copy()
print(b)
b[1][0] = 0
print(a)
print(b)