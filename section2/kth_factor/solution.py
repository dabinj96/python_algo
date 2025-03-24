import sys
#sys.stdin = open('in4.txt', 'rt')

n, k = map(int, input().split())
cnt = 0

for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print("This is kth factor: ", i)
        break
else:
    print(-1)