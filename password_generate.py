from string import ascii_letters, digits
from random import choice
lst = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))
amount = int(input())
lenght = int(input())
while amount > 0:
    for i in range(lenght):
        result = ''
        result += choice(lst)
        print(*result, end='')
    print()
    amount -= 1