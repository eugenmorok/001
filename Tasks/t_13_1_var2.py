"""
Необходимо использовать функции. Программа должна поддерживать следующие арифметические операции:
+, -, /, *, %(получение процента от числа), **(возведение в квадрат), **х(возведение в степень числа х).
Запрещено подключать дополнительные модули. Для вывода результата необходимо использовать функцию print().
"""
args = input().replace("**", "$")

print(args)

op = ""
ops = ("$", "+", "-", "/", "*", "%", "/")

for item in args:
    if item in ops:
        op = item

op_idx = args.find(op)

result = 0
print(op)

if op == "%":
    result = int(args[:op_idx]) / 100

else:
    first = 0
    list = 0

    first = int(args[:op_idx])
    last = int(args[op_idx + 1:])

    print(first, op, last)

print(result)
