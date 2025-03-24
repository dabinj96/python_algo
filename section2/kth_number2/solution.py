import sys
sys.stdin = open("in3.txt", "rt")

n, k = map(int, input().split())
a = list(map(int,input().split()))

res = set()
for i in range(n):
    for j in range(i+1,n):
        for h in range(j+1,n):
            if a[i] + a[j] + a[h] not in res:
                res.add(a[i] + a[j] + a[h])
    
res = sorted(res, reverse=True)
print(res[k-1])



                 