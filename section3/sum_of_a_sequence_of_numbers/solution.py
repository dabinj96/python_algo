import sys
sys.stdin = open('in4.txt', 'rt')

n, m = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
left, right = 0, 1
curr = a[left]

while True:
    if curr < m:
        if right < n:
            curr += a[right]
            right += 1
        else:
            break
    elif curr == m:
        cnt += 1
        curr -= a[left]
        left += 1
    else:
        curr -= a[left]
        left += 1

print(cnt)
          
        