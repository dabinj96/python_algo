import sys
sys.stdin = open("in2.txt", "rt")

n = int(input())
a = []
max_sum = 0

for _ in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1+=a[i][j] # Rows
        sum2+=a[j][i] # Cols
    max_sum = max(max_sum, sum1, sum2)

sum1=sum2=0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
max_sum = max(max_sum, sum1, sum2)

print(max_sum)
    
        


        
        
    

