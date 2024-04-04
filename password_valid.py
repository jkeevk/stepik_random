
def is_valid_password(password):
    password = password.split(sep=':')
    if len(password) != 3:
        return False
    print(password)
    flag = True
    a, b, c = password[0], int(password[1]), int(password[2])
    if a == a[::-1]:
        flag = True
    else:
        return False
    
    for i in range(2, int(b ** 0.5) + 1):
        if b % i == 0:
            return False
    if b > 1 and flag == True:
        flag = True
    else:
        return False
    if int(c) % 2 == 0:
        flag = True
    else:
        return False
    return flag
   
print(is_valid_password('15551:7:290'))