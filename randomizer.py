import random

num1 = random.randint(0, 17)
num2 = random.randint(-5, 5)

num = random.randrange(10)
numfloat = random.random()
numfloat2 = random.uniform(1.5, 17.3)

print(num1)
print(num2)
print(num)
print(numfloat)
print(numfloat2)

# random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел

for _ in range(10):
    print(random.randint(1, 100))

# from random import *
# позволяет в дальнейшем не писать название модуля и символ точки при вызове функций модуля.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)
print(numbers)


print(random.choice('BEEGEEK'))
print(random.choice([1, 2, 3, 4]))
print(random.choice(['a', 'b', 'c', 'd']))

numbers = [2, 5, 8, 9, 12]

print(random.sample(numbers, 1))
print(random.sample(numbers, 2))
print(random.sample(numbers, 3))
print(random.sample(numbers, 5))