import sys
sys.stdin = open('input.txt')
N = int(sys.stdin.readline())
ant = []

for i in range(N):
    arr = list(map(str, sys.stdin.readline().split()))
    ant.append(arr[1:])

ant.sort()

for i in range(N):
    if i == 0:
        for j in range(len(ant[i])):
            print("--" * j + ant[i][j])
    else:
        count = -1
        for j in range(len(ant[i])):
            if len(ant[i - 1]) <= j or ant[i - 1][j] != ant[i][j]:
                break
            else:
                count = j
        for j in range(count + 1, len(ant[i])):
            print("--" * j + ant[i][j])