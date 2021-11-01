import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 9)

def sol(start, right):
    end = right+1
    if start > right:
        return
    for i in range(start+1, right+1):
        if lista[start] < lista[i]:
            end = i
            break
    sol(start+1, end-1)
    sol(end, right)
    print(lista[start])


lista = []
for i in range(10000):
    try:
        n = int(sys.stdin.readline().strip())
        lista.append(n)
    except:
        break

sol(0, len(lista)-1)


