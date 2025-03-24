import sys
sys.stdin = open("in3.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
cnt = 0
total = 0

for i in range(n):
    if a[i] == 1:
        cnt += 1
        total += cnt
    else:
        cnt = 0

print(total)