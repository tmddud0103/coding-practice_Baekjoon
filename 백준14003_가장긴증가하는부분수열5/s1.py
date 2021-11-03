import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().rstrip())
ll = list(map(int, input().split()))
temp = [1000000001, ll[-1]]
ans = []
for i in range(N-2, -1, -1):
    if temp[-1] > ll[i]:
        temp.append(ll[i])
    else:
        for j in range(len(temp)-1, -1, -1):
            if ll[i]<=temp[j]:
                temp[j+1] = ll[i]
                break
    if len(ans) < len(temp)-1:
        ans = temp[1:]
print(len(temp)-1)
for i in range(len(ans)-1, -1, -1):
    print(ans[i], end=' ')
