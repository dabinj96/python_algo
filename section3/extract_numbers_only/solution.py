import sys
sys.stdin = open("in4.txt", "rt")

word = input()
numbers = ('0','1','2','3','4','5','6','7','8','9')
res_num = 0

for c in word:
    if c in numbers:
        res_num = res_num * 10 + int(c)

res_cnt = 0
for i in range(1,res_num+1):
    if res_num%i == 0:
        res_cnt += 1

print(res_num, end='\n')
print(res_cnt)
    