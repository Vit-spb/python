# Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# Выведите yes или no соответственно.
a = 3
b = 2
c = 4

# Введите ваше решение ниже
if (c % a == 0 or c % b == 0):
    print("yes")
else:
    print("no")