# объявление функции
def convert_to_python_case(text):
    words = []
    for i in text:
        if i.lower() == i:
            words.append(i)
        if i.upper() == i and i.upper():
            words.append('_')
            words.append(i)
    result = ''.join(words).replace('_', '', 1)
       
    print(result.lower())

# считываем данные
txt = 'TSSSSss%523523@@@asds@@#'

# вызываем функцию
print(convert_to_python_case(txt))
