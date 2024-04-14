s = []
for i in range(int(input())):
    s.append(input().split(': '))
dct = {}
w = []
for i in range(int(input())):
    w.append(input()) 
for i in s:
    dct[i[0].lower()] = i[1]
for i in w:
    if dct.get(i.lower(), False) is False:
        print('Не найдено')
    else:
        print(dct[i.lower()])