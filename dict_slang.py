string = [input().split(': ') for i in range(int(input()))]
dictionary = {}
words = [input() for i in range(int(input()))]
for i in string:
    dictionary[i[0].lower()] = i[1]
for i in words:
    if dictionary.get(i.lower(), False) is False:
        print('Не найдено')
    else:
        print(dictionary[i.lower()])