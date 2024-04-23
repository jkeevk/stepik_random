n, m = [int(i) for i in input().split()]
matrix_1 = [input().split() for _ in range(n)]
input()
matrix_2 = [input().split() for _ in range(n)]
matrix_3 = [[0]*m for _ in range(n)] 
for i in range(n):
    for j in range(m):
        matrix_3[i][j] = int(matrix_1[i][j]) + int(matrix_2[i][j])
for i in matrix_3:
    print(*i)