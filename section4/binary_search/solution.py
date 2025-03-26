import sys
sys.stdin = open("in4.txt", "rt")

n, target = map(int, input().split())
a = list(map(int, input().split()))

sorted_array = sorted(a)

start, end = 0, n-1
while start <= end:
    mid = (start+end) // 2
    if sorted_array[mid] > target:
        end = mid - 1
    elif sorted_array[mid] < target:
        start = mid + 1
    else:
        print(mid+1)
        break