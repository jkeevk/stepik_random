i = 499
counter = 0
if i >= 25:
    b = i // 25
    counter += b
    if (i % 25) > 10:
        b = (i % 25) // 10
        counter += b
    if ((i % 25) % 10) > 5:
        b = ((i % 25) % 10) // 5
        counter += b
    if (((i % 25) % 10) % 5) >= 1:
        b = (((i % 25) % 10) % 5) // 1
        counter += b
if 10 <= i < 25:
    b = i // 10
    counter += b
    if (i % 10) > 5:
        b = (i % 10) // 5
        counter += b
    if ((i % 10) % 5) >= 1:
        b = ((i % 10) % 5) // 1
        counter += b
if 5 <= i < 10:
    b = i // 5
    counter += b
    if (i % 5) >= 1:
        b = (i % 5) // 1
        counter += b
if 1 <= i < 5:  
    b = i // 1
    counter += b    
print(counter)