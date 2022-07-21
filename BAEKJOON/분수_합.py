import math


up1, down1 = tuple(map(int, input().split(" ")))
up2, down2 = tuple(map(int, input().split(" ")))

down = down1 * down2
up = up1 * down2 + up2 * down1

gcd = math.gcd(up, down)

up = up // gcd
down = down // gcd

print(int(up), int(down))