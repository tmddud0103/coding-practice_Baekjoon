import sys
import heapq
sys.stdin = open('input.txt')

def asdasd(mat, end):
    mat.sort()
    i, j, n = 0, 0, len(mat)
    que = []
    while i < end+1:
        while j < n and i >= mat[j][0]:
            heapq.heappush(que, mat[j][::-1])
            j += 1
        if not que:
            if j == n:
                return True
            i = mat[j][0]
            continue
        if que[0][0] < i:
            return False

        heapq.heappop(que)
        i += 1
    if que:
        return False
    else:
        return True


for TEST in range(int(sys.stdin.readline())):
    m, n = map(int,sys.stdin.readline().split())
    mat = []
    for i in range(n):
        a, b = map(int,sys.stdin.readline().split())
        if a <= b:
            mat.append((a,b))
            mat.append((a+m, b+m))
        else:
            mat.append((a, b+m))
    kk = asdasd(mat, 2*m)

    if n <= m and kk:
        print("YES")
    else:
        print("NO")
