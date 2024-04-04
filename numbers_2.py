n = 56689932106
string = str(n)
sum5 = 0
mult7 = 1
ag0_5 = 0
print(string.count('3'))
print(string.count(str(n % 10)))
counter = 0
for i in range(len(string)):
    if (n % 10) % 2 == 0:
        counter += 1
    if (n % 10) > 5:
        sum5 += (n % 10)
    if (n % 10) > 7:
        mult7 *= (n % 10)
    if (n % 10) == 0:
        ag0_5 += 1
    elif (n % 10) == 5:
        ag0_5 += 1
    n //= 10
print(counter) 
print(sum5)
print(mult7)
print(ag0_5)
       