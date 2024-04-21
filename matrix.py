n = int(input())
matrix = []
for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
counter_top, counter_right, counter_bottom, counter_left = 0, 0, 0, 0
for i in range(n):
    for j in range(n):
        if i == j or i + j + 1 == n:
            pass
        elif j <= i <= n-1-j:
            counter_left += int(matrix[i][j])
        elif j >= i <= n-1-j:
            counter_top += int(matrix[i][j])
        elif j >= i >= n-1-j:
            counter_right += int(matrix[i][j])
        elif j <= i >= n-1-j:            
            counter_bottom += int(matrix[i][j])
print(f'Верхняя четверть: {counter_top}')
print(f'Правая четверть: {counter_right}')
print(f'Нижняя четверть: {counter_bottom}')
print(f'Левая четверть: {counter_left}')