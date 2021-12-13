import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
s = [0 for _ in range(10)]

first = 1

while n != 0:
    while n % 10 != 9:
        for i in str(n):
            s[int(i)] += first
        n -= 1
    if n < 10:
        for i in range(n + 1):
            s[i] += first
        s[0] -= first
        break
    else:
        for i in range(10):
            s[i] += (n // 10 + 1) * first
    s[0] -= first
    first *= 10
    n //= 10
for i in s:
    print(i, end=' ')