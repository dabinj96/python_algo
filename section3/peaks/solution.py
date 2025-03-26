import sys
sys.stdin = open("in3.txt", 'rt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

padded = [[0] * (n + 2) for _ in range(n + 2)]
for i in range(n):
    for j in range(n):
        padded[i + 1][j + 1] = a[i][j]

cnt = 0
directions = [(-1,0), (1,0), (0,-1), (0,1)]

for i in range(1, n + 1):
    for j in range(1, n+1):
        current = padded[i][j]
        if all(current > padded[i + dx][j + dy] for dx, dy in directions):
            cnt += 1

print(cnt)
