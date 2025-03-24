import sys
sys.stdin = open("in5.txt", "rt")

n, m = map(int, input().split())

cnt = [0] * (n+m+2)
max_num = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1
        
for i in range(len(cnt)):
    if cnt[i] > max_num:
        max_num = cnt[i]

for i in range(len(cnt)):
    if cnt[i] == max_num:
        print(i, end=' ')