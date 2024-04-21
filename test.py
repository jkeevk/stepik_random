n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
counter = 0
for i in range(n):
    for j in range(n):
        if i == j or i + j + 1 == n:
            pass
        elif j <= i <= n-1-j:
            counter += int(matrix[i][j])
print(counter)

    


values = [{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]
merge(values)
