'''Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 '''

x = [2, 3, 5, 9, 3]

odd_index = [y for x,y in enumerate(x) if x%2 != 0]
print(sum(odd_index))