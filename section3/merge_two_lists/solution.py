import sys
sys.stdin = open('in4.txt', 'rt')

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

res = []
i, j = 0, 0

while i < n and j < m:
    if a[i] <= b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1

if i < n:
    res = res + a[i:]
if j < m:
    res = res + b[j:]

print(res)
    
    
        
        