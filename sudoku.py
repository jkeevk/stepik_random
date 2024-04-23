n = int(input())
lst = []
for i in range(1, n**2 + 1):
    lst.append(i)
matrix = [input().split() for _ in range(n)]
res = []
flag = True
for i in matrix:
    for j in i:
        if int(j) in lst:
            res.append(int(j))
if set(res) != set(lst):
    flag = False
sum = 0
if flag == True:
    for i in matrix:
        res = 0
        for j in i:
            sum += int(j)
            res += int(j)
    if sum / res != len(matrix):
        flag = False
sum, diag, diag2 = 0, 0, 0
if flag == True:
    for i in range(n):
        res = 0
        for j in range(n):
            sum += int(matrix[j][i])
            res += int(matrix[j][i])
            if i + j + 1 == n:
                diag += int(matrix[j][i])
            if i == j:
                diag2 += int(matrix[j][i])
    if diag != diag2:
        flag = False
    if sum / res != len(matrix):
        flag = False
if flag:
    print('YES')
else:
    print('NO')