import sys
sys.stdin = open('input.txt')

n = '0' + str(sys.stdin.readline().rstrip())
m = '0' + str(sys.stdin.readline().rstrip())
n_len = len(n)
m_len = len(m)
mat = [[0] * n_len for _ in range(m_len)]
for i in range(1, m_len):
    for j in range(1, n_len):
        if m[i] == n[j]:
            mat[i][j] = mat[i - 1][j - 1] + 1
        else:
            mat[i][j] = max(mat[i - 1][j], mat[i][j - 1])
print(max(mat[-1]))
# print(mat[-1])
# print(mat)
ans = ''
i = m_len-1
j = n_len-1
while i != 0:
    if mat[i][j] == 0:
        break
    if mat[i][j] == mat[i-1][j]:
        i -= 1
    elif mat[i][j] == mat[i][j-1]:
        j -= 1
    else:
        ans = n[j] + ans
        i -= 1
        j -= 1
print(ans)