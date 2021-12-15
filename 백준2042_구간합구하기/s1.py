import sys
sys.stdin = open('input.txt')

def make_tree(start, end, node):
    if start == end:
        tree[node] = nList[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = make_tree(start, mid, node * 2) + make_tree(mid + 1, end, node * 2 + 1)
    return tree[node]


def summit(start, end, node, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start+end) // 2
    return summit(start, mid, node*2, left, right) + summit(mid + 1, end, node*2+1, left, right)


def change(start, end, node, index, diff):
    if index < start or index > end:
        return

    tree[node] += diff
    if start == end:
        return

    mid = (start+end) // 2
    change(start, mid, node*2, index, diff)
    change(mid + 1, end, node * 2 + 1, index, diff)


n, m, k = map(int, sys.stdin.readline().split())
nList = []
tree = [0] * (4 * n)

for i in range(n):
    nList.append(int(sys.stdin.readline()))

make_tree(0, n - 1, 1)

for i in range(m + k):
    temp = list(map(int, sys.stdin.readline().split()))

    if temp[0] == 1:
        temp[1] -= 1
        diff = temp[2] - nList[temp[1]]
        nList[temp[1]] = temp[2]
        change(0, n - 1, 1, temp[1], diff)
    elif temp[0] == 2:
        print(summit(0, n - 1, 1, temp[1] - 1, temp[2] - 1))