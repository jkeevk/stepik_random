str = 'London is the capital of Great Britain. More than six million people live in London. London lies on both banks of the river Thames. It is the largest city in Europe and one of the largest cities in the world. London is not only the capital of the country, it is also a very big port, one of the greatest commercial centres in the world, a university city, and the seat of the government of Great Britain!'
lst = [word.strip('.,!?:;-') for word in str.lower().split()]

result = {}
for t in lst:
    result[t] = result.get(t, 0) + 1
res = sorted(result.items(), key=lambda x: (x[1], x[0]))
print(res[0][0])