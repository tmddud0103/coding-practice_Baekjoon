import sys
import math
sys.stdin = open('input.txt')
X = 1000000007
M = int(sys.stdin.readline().rstrip())

def asd(num, exp):
    if exp == 1:
        return num
    if exp % 2 == 0:
        half = asd(num, exp//2)
        return half * half % X
    else:
        return num * asd(num, exp - 1) % X

def qwe(n, s):
    return s * asd(n, X-2) % X

sum = 0
for _ in range(M):
    n, s = map(int, sys.stdin.readline().split())
    gcd = math.gcd(n, s)
    n //= gcd
    s //= gcd
    sum += qwe(n, s)
    sum %= X

print(sum)

