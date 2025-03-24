import sys
sys.stdin = open("in4.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
max_sum = 0

def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10
    return total

for x in a:
    if digit_sum(x) > max_sum:
        res = x
        max_sum = digit_sum(x)
        
print(res)