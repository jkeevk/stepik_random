string = 'Дорог Рим город или дорог Миргород?!'
no_spaces = [i for i in string if i.isalpha()]
lowers = (''.join(no_spaces).lower())
if lowers == lowers[::-1]:
    print('YES')
else:
    print('NO')