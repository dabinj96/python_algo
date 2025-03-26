import sys
sys.stdin = open("in4.txt", "rt")

card = list(range(21))

for _ in range(10):
    a, b = map(int,input().split())
    cnt = 0
    for i in range((b-a+1)//2):
        card[a+i], card[b-i] = card[b-i], card[a+i]
    """
    for i in range(a-1, b):
        if cnt < (b-a+1)//2:
            tmp = card[i]
            card[i] = card[b-1-cnt]
            card[b-1-cnt] = tmp
            cnt += 1
    """
print(card[1::])