import random

print('Привет сенсей!')

# Задача-1:

print('Представим себе, что вы голодны и хотите сходить в магазин')
array = []
print('Начинаем составлять список покупок')
for i in range(5):
    array.append(input('Введите что необходимо купить: '))
    (array[i]) = str.lower(array[i])

count = 0

for x in array:
    count = count + 1
    print('{}.{:>15}'.format(count, x))

# Задача-2:

print('Перед выходом из дома к Вам домой приходит старый друг, который уже зашел в магазин и купил часть продуктов')
print('Теперь необходимо убрать из Вашего списка те продукты, которые уже принёс товарищ')

b = ['яблоко', 'груша', 'виноград', 'пиво', 'дыня']
new_array = list(set(array) - set(b))
print('Ваш новый список выглядит примерно так:')
count = 0
for i in new_array:
    count = count + 1
    print('{}.{:>15}'.format(count, i))

# Задача-3:

numbers = []
for _ in range(10):
    numbers.append(random.randint(0, 50))
print('Итак, у нас есть список: ', numbers)
print('Теперь магическим образом будем получать новый список')
new_numbers = []

for r in numbers:
    if r % 2 == 0:
        new_numbers.append(r / 4)
    else:
        new_numbers.append(r * 2)
print(new_numbers)
