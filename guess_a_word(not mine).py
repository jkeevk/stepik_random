from math import log2, ceil

def is_valid(znach):
    return znach.isdigit() and 1 <= int(znach) 

def game(left, right):
    count, kon = 0, ceil(log2(int(right)))
    while True:
        left,  right = int(left), int(right)
        midle = (left + right) // 2  
        print('Загаданное число', midle, '? Введи "=", если равно!')
        resh = input('">", если больше и "<", если меньше')
        if resh != "=" and resh != ">" and resh != "<":
            print('Не совсем ясно... Больше или меньше?')
        elif count == kon:
            return print("Вы пытаетесь меня обмануть!")
        elif resh == '>':
            right = midle - 1
            count += 1
        elif resh == '<':
            left = midle + 1
            count += 1
        elif resh == '=':
                count += 1
                return print('Здорово! Я угадал за ', count, 'попыток')
            
def begin_game():
    while True:  
        left = input('Давай решим какой будет минимальный порог? ')
        right = input('Давай решим какой будет максимальный порог? ')
        if is_valid(left) == False or is_valid(right) == False:
            print('Я угадываю только целые числа больше единицы, попробуй еще?')
            continue
        else:
            return left, right

def repit():
    l = ''
    while l.upper() != "ДА" or l.upper() != "НЕТ":
        l = input('Сыграем еще? Да/Нет? ').upper()
        if l == "ДА":
            print('Сыграем еще раз!')
            return False
        elif l == 'НЕТ':
            print('До свидания. Еще увидимся...')
            return True
    
print('Добро пожаловать в числовую угадайку. Но угадывать теперь буду я))')
flag = False
while flag != True:
    left, right = begin_game()

    game(left, right)

    flag = repit()