import sys
sys.stdin = open("in3.txt", 'rt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

res = 0
e=s=n//2

for i in range(n):
    for j in range(s,e+1):
        res += a[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)