# DZ_22.9.1_(HW-03)
# Двоичный поиск

import sys
def binary_search(array, element, left, right):
    if left > right: # если левая граница превысила правую,
            return False # значит элемент отсутствует

    middle = (right + left) // 2 # находим середину
    if element == array[middle]: # если элемент в середине,

        if array[middle - 1] < element and element <= array[middle]: # и если это число больше предыдущего и при этом меньше или равно следующему
            return middle # возвращаем индекс этого элемента
        elif element < array[middle]: # если элемент меньше элемента в середине
            return binary_search(array, element, left, middle - 1) # рекурсивно ищем в левой половине
    elif element == array[middle - 1]: # если это число равно элементу слева от середины
            return binary_search(array, element, left, middle - 1) # возвращаем индекс этого элемента
    else:
            return binary_search(array, element, middle + 1, right) # иначе рекурсивно ищем в правой половине


try:
    array = list(map(int, input("Введите целые числа в любом порядке, через пробел: ").split()))
except ValueError:
    print('Ошибка! Вводить можно только целые числа.')
    sys.exit()

element = int(input("Введите любое целое число из введеного списка: "))
array = sorted(array)
print(array)
left = int(array[0])
right = int(array[-1])
if element < left or element > right:
    print('Число не входит в диапазон списка! Введите любое целое число из введеного списка: ')
else:
    print(binary_search(array, element, 0, len(array) - 1))
