import sys
sys.stdin = open('input.txt')

n, s = list(map(int, sys.stdin.readline().split()))
nlist = list(map(int, sys.stdin.readline().split()))
sum_list = [0]*(n+1)
for i in range(1, n+1):
    sum_list[i] = sum_list[i-1] + nlist[i-1]
start = 0
end = 1
ans = 10000000000
while start != n:
    if sum_list[end] - sum_list[start] >= s:
        if end - start < ans:
            ans = end - start
        start += 1
    else:
        if end < n:
            end += 1
        else:
            start += 1
if ans == 10000000000:
    print(0)
else:
    print(ans)
