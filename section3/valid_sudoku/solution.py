import sys
sys.stdin = open("in4.txt", 'rt')

a = [list(map(int, input().split())) for _ in range(9)]

def is_valid_group(group):
    """Check if a group (row, column, or subgrid) contains unique numbers 1-9."""
    group = [num for num in group if num != 0]  # Exclude zeros (if grid allows empty cells)
    return len(group) == len(set(group))

def valid_sudoku(grid):
    # Check rows and columns
    for i in range(9):
        if not is_valid_group(grid[i]) or not is_valid_group([grid[j][i] for j in range(9)]):
            return False

    # Check 3x3 subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_valid_group(subgrid):
                return False

    return True

if valid_sudoku(a):
    print("YES")
else:
    print("NO")









