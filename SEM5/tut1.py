# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.

def f(a,b):
        rek=int(a)
        for _ in range(1, b):
            rek*=a
        return rek
a = 3
b = 5
print(f(a, b))