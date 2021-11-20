import sys
sys.stdin = open('input.txt')

row_ch = [[0]*10 for _ in range(10)]
col_ch = [[0]*10 for _ in range(10)]
cube_ch = [[0]*10 for _ in range(10)]
mat = []
for i in range(9):
    temp = list(map(int, sys.stdin.readline().rstrip()))
    for j in range(9):
        n = temp[j]
        row_ch[i][n] = 1
        col_ch[j][n] = 1
        cube_ch[(i//3)+3*(j//3)][n] = 1
    mat.append(temp[:])

goto = 0

def sudoku(cnt):
    global goto
    i = (cnt // 9)
    j = (cnt % 9)
    if cnt == 81:
        goto = 1
        return
    elif mat[i][j] != 0:
        sudoku(cnt + 1)
    else:
        for k in range(1, 10):
            if row_ch[i][k] == 0 and col_ch[j][k] == 0 and cube_ch[(i//3)+3*(j//3)][k] == 0:
                row_ch[i][k] = 1
                col_ch[j][k] = 1
                cube_ch[(i // 3) + 3 * (j // 3)][k] = 1
                mat[i][j] = k
                sudoku(cnt + 1)
                if goto == 1:
                    return
                row_ch[i][k] = 0
                col_ch[j][k] = 0
                cube_ch[(i // 3) + 3 * (j // 3)][k] = 0
                mat[i][j] = 0
        if mat[i][j] == 0:
            return

sudoku(0)
for i in range(9):
    print(''.join(map(str,mat[i])))
