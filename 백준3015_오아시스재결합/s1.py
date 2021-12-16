import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().strip())
stack = []

ans = 0
for _ in range(n):
    x = int(sys.stdin.readline().strip())
    while stack and stack[-1][0] < x:
        ans+= stack.pop()[1]
    if stack and stack[-1][0] == x:
        cnt = stack.pop()[1]
        ans+= cnt
        if len(stack) != 0 :
            ans += 1
        stack.append((x, cnt+1))
    else:
        if len(stack) != 0 :
            ans += 1
        stack.append((x, 1))
print(ans)