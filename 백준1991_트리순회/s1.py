import sys
sys.stdin = open('input.txt')
def slr(a):
    global temp1, left, right, alpa, temp2, temp3
    temp1 += a
    if alpa[a][0] != '.':
        # temp1 += alpa[a][0]
        slr(alpa[a][0])
    temp2 += a
    if alpa[a][1] != '.':
        # temp1 += alpa[a][1]
        slr(alpa[a][1])
    temp3 += a



n = int(sys.stdin.readline().lstrip())
center = [0]*n
left = [0]*n
right = [0]*n
alpa = dict()
for i in range(n):
    c, l, r = list(map(str, sys.stdin.readline().split()))
    alpa[c] = [l,r]

    center[i] = c
    left[i] = l
    right[i] = r
q = ['A']
temp1 = ''
temp2 = ''
temp3 = ''
slr('A')
print(temp1)
print(temp2)
print(temp3)