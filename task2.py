#Задача 2
#Найдите сумму цифр трехзначного числа.
#Пример:
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

x=int(input('Введите трехзначное число: '))
s=str(x)
a = int(s[0])
b = int(s[1])
c = int(s[2])
print(f'сумма цифр равна: {a+b+c}')