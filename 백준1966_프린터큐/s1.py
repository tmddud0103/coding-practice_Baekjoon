import sys
sys.stdin = open('input.txt')


TC = int(sys.stdin.readline().lstrip())

for _ in range(TC):
    n, m = list(map(int, sys.stdin.readline().split()))
    imp = list(map(int, sys.stdin.readline().split()))
    idx = list(range(len(imp)))
    idx[m] = 'target'

    order = 0

    while True:
        if imp[0] == max(imp):
            order += 1
            if idx[0] == 'target':
                print(order)
                break
            else:
                imp.pop(0)
                idx.pop(0)

        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))