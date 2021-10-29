import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().rstrip())
ll = list(map(int, input().split()))
temp = [0, ll[0]]
for i in range(1, N):
    if temp[-1] < ll[i]:
        temp.append(ll[i])
    else:
        for j in range(len(temp)-1, 0, -1):
            if temp[j]>=ll[i]>temp[j-1]:
                temp[j] = ll[i]
                break
print(len(temp)-1)
