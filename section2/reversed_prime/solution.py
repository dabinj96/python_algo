import sys
sys.stdin = open("in4.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

def reverse(x):
    res = 0
    while x > 0:
        tmp = x % 10
        res = res * 10 + tmp
        x = x // 10
    return res
        
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    else:
        return True

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')