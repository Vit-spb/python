# Найдите сумму цифр трехзначного числа n.

# Результат сохраните в перменную res.
n =507

# Введите ваше решение ниже

res = n//100 + (n%100)//10 + n%10
print(res)