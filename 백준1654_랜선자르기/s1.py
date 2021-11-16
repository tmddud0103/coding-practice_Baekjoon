import sys
sys.stdin = open('input.txt')

k, n = map(int, sys.stdin.readline().split())
klist = [ int(sys.stdin.readline().rstrip()) for _ in range(k)]
start = 0
end = max(klist)

max_len = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    if mid ==0:
        mid += 1
    for i in range(k):
        cnt += klist[i]//mid
    # print(mid, cnt)
    if cnt >= n:
        if max_len < mid:
            max_len = mid
        start = mid + 1
    elif cnt < n:
        end = mid - 1

print(max_len)
