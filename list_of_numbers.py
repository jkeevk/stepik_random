# объявление функции
def quick_merge(numbers):
    fill_list.sort()
    res = list(map(str, fill_list))
    result = ' '.join(res)
    return result

# считываем данные
lists = int(input())
fill_list = []
for _ in range(lists):
    numbers = [int(c) for c in input().split()]
    for i in numbers:
        fill_list.append(i)
    
# вызываем функцию
print(quick_merge(numbers))