import sys
sys.stdin = open("in3.txt", "rt")

n = int(input())

for i in range(n):
    word = input()
    word = word.lower()
    if word == word[::-1]:
        print("#%d Yes" %(i+1), end='\n')
    else:
        print("#%d No" %(i+1), end='\n')