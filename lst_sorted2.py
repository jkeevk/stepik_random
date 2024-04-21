book = {}
for _ in range(int(input())):
    name, product, count = input().split()
    book.setdefault(name, {})
    book[name][product] = book[name].get(product, 0) + int(count)
for name, purchase in sorted(book.items()):
    print(name + ':')
    for product in sorted(purchase):
        print(product, purchase[product])
    


values = [{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]
merge(values)
