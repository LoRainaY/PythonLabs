"""
Вариант 5
1.Найдите наименьший четный элемент списка. Если такого нет, то выведите
первый элемент.
2.Преобразовать список так, чтобы сначала шли нулевые элементы, а затем
все остальные.
"""
# 1
numbersList = [int(i) for i in input('Введите значения через пробел ').split()]

print(numbersList)  # вывод первонач. списка

numbersList.sort()  # сортировка списка на возрастанию

print(numbersList)  # вывод отсортированного списка

print("Минимальное четное число: ")
for i in numbersList:  # поиск первого четного элемента из отсортированного списка
    if i % 2 == 0 and i != 0:
        print(i)
        break

