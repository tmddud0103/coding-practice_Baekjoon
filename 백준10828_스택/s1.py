import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    k = list(map(str, sys.stdin.readline().split()))
    if k[0] == 'push':
        stack.append(int(k[1]))
    elif k[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif k[0] == 'size':
        print(len(stack))
    elif k[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif k[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])