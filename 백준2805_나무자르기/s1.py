import sys
sys.stdin = open('input.txt')

N, M = map(int,sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
start, end = 0, max(trees)

while start <= end:
    length = 0
    mid = (start+end)//2
    length = sum(i-mid if i> mid else 0 for i in trees)
    if length == M:

        break
    elif length > M:

        start = mid + 1
    else:
        end = mid + 1


print(mid)