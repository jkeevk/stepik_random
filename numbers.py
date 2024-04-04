a = 5678
summary = 0
counter = 0
multiply = 1
average = 0
last_digit = a % 10
while a > 0:
    very_last_digit = a % 10
    summary += last_digit
    counter += 1
    multiply *= last_digit
    average = summary / counter
    a = a // 10
print(summary)
print(counter)
print(multiply)
print(average)
print(last_digit)
print(a + (last_digit % 10))