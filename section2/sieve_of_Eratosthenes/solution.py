import sys
sys.stdin = open("in4.txt", "rt")

n = int(input())
ch = [0] * (n+1)
cnt = 0

for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1

print(cnt)
"""
prime = [True] * (n+1)
prime[0] = prime[1] = False

for i in range(2, int(n**0.5)+1):
    if prime[i]:
        for j in range(i*i, n+1, i):
            prime[j] = False
            
print(len([i for i in range(n+1) if prime[i]]))
"""