# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

list_1 = [1, 2, 3, 4, 5]
k = 4

# Введите ваше решение ниже
dif = 0
min_dif = k
result = list_1[1]
for i in list_1:
    if i - k == 0:
        result = i
        break
    else:
        dif = k - i
        if abs(dif) < abs(min_dif):
            min_dif, result = dif, i
print(result)