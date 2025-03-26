import sys
sys.stdin = open("in5.txt", "rt")
board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

for i in range(3):  # Loop for 5-length horizontal and vertical palindromes
    for j in range(7):
        # Check 5-length horizontal palindrome
        if board[j][i:i+5] == board[j][i:i+5][::-1]:
            cnt += 1
        # Check 5-length vertical palindrome (optimized to check first 2 pairs)
        if board[i][j] == board[i+4][j] and board[i+1][j] == board[i+3][j]:
            cnt += 1

print(cnt)