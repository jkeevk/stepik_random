#1

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
res = input() + ' запретил букву'
for j in alphabet:
    if j in res:
        print(' '.join(res.lstrip().split()), j)
    if len((set(res.lstrip()))) == 1:
        break
    for i in res:
        if j == i:
            res = res.replace(j, '')


# #2
            
# alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# word = input() + ' запретил букву'
# for letter in alphabet:
#     if letter in word:
#         print(word.strip(), letter)
#         word = word.replace(letter, '').replace('  ', ' ').strip()


# # Генерация строчного алфавита
# alpha = [chr(i) for i in range(1072, 1104)]
# print(alpha)
