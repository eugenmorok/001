"""
Задан список с числами. Напишите программу, которая выводит все элементы списка, которые больше предыдущего,
в виде отдельного списка.
"""

list = [ 1, 5, 1, 5, 1]

new_list = []

for i in range(1, len(list)):
    if list[i] > list[i - 1]:
        new_list.append(list[i])

print(new_list)
