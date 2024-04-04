# объявление функции
def solve(a, b, c):
    from math import sqrt
    d = b**2 - (4 * a * c)
    if d > 0:
        x1 = (-b + sqrt(d))/(2 * a)
        x2 = (-b - sqrt(d))/(2 * a)
        if x1 > x2:
            return x2, x1
        else:
            return x1, x2
    elif d == 0:
        x1 = -b/(2 * a)
        return x1

# считываем данные
a, b, c = -1, -4, -5

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)