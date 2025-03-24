import sys
sys.stdin = open("in4.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
total = 0

for i in range(n):
    total += a[i]

ave = round(total/n)
min_distance = 100

for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min_distance:
        min_distance = tmp
        score = x
        res = idx + 1
    elif tmp == min_distance:
        if x > score:
            score = x
            res = idx + 1

print(ave, res)