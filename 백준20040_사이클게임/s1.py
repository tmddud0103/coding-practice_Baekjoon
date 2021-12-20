import sys
sys.stdin = open('input.txt')


n, m = list(map(int, sys.stdin.readline().split()))
parents = [i for i in range(n)]
answer = 0

def find(x):
    if x == parents[x]:
        return x
    else:
        y = find(parents[x])
        parents[x] = y
        return y

def asd(x, y, indx):
    global answer
    x = find(x)
    y = find(y)
    if x != y:
        parents[max(x,y)] = min(x,y)
    elif answer == 0:
        answer = indx

for i in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    asd(a, b, i + 1)

print(answer)