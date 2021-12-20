import sys
sys.stdin = open('input.txt')

N = 4000001
factorial = [1] * N
for i in range(1, N):
    factorial[i] = (factorial[i - 1] * i) % 1000000007

for _ in range(int(input())):
    n, k = list(map(int, sys.stdin.readline().split()))

    A = factorial[n]
    B = (factorial[k] * factorial[n - k]) % 1000000007

    B2 = 1
    expo = 1000000007 - 2
    while expo:
        if expo % 2: B2 = (B * B2) % 1000000007
        B = (B * B) % 1000000007
        expo //= 2

    res = (A * B2) % 1000000007
    print(res)
