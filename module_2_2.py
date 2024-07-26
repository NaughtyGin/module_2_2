first = int(input('Введите 1-е число: '))
# print(first)
second = int(input('Введите 2-е число: '))
# print(second)
third = int(input('Введите 3-е число: '))
# print(third)
if first == second and second == third:
    print('Количество одинаковых чисел: 3')
elif first == second or second == third or first == third:
    print('Количество одинаковых чисел: 2')
else: print('Количество одинаковых чисел: 0')