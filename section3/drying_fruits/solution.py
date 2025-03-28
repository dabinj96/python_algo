import sys
sys.stdin = open("in4.txt", 'rt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

s, e = 0, n-1
res = 0
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        e -= 1
        s += 1
    else:
        e += 1
        s -= 1

print(res)
            

    