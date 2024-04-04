original_value = 4  # Ваше исходное значение
values = [3, 7, 8, 2, 9]  # Список значений для перебора
found = False  # Флаг, указывающий на то, найдено ли искомое число

for value in values:
    if value == original_value:
        print(value)
        found = True

if not found:
    print("Искомое число не найдено в списке")