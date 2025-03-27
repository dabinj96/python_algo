import sys
sys.stdin = open('in3.txt', 'rt')

k, n = map(int, input().split())
cables = list()
res = 0
longest = 0

def count(length, cables):
    cnt = 0
    for x in cables:
        cnt += (x // length)
    return cnt

for i in range(k):
    tmp =int(input())
    cables.append(tmp)
    longest = max(longest, tmp)
    
shortest = 1
while shortest <= longest:
    mid = (shortest+longest) // 2
    if count(mid, cables) >= n:
        res = mid
        shortest = mid + 1
    else:
        longest = mid - 1
        
print(res)
