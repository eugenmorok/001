"""
Пароль считается надежным, если его длина составляет не менее 12 символов, при этом он должен содержать хотя
бы одну заглавную букву, хотя бы одну строчную букву, хотя бы одну цифру и хотя бы один спецсимвол. Напишите
код, который обрабатывает строковые данные и выводит сообщение о том, надежен ли пароль или нет. В случае,
если пароль не надежен, код должен выдавать рекомендации для усиления надежности пароля.


Подставьте "Входные данные" в свою программу и сравните результат с выходными данными.
1) Входные данные: 'qwerty'.
     Выходные данные: 'Слабый пароль. Рекомендации: увеличить число символов - 6,
     добавить 1 заглавную букву, добавить 1 цифру, добавить 1 спецсимвол '
2) Входные данные: 'Qwert_Y'.
     Выходные данные: 'Ошибка. Запрещенный спецсимвол'
3) Входные данные: 'Q123wer123tY'.
     Выходные данные: 'Слабый пароль. Рекомендации: добавить 1 спецсимвол'
4) Входные данные: '@PowerRangers123@'.
     Выходные данные: 'Сильный пароль.'
"""

line = "a763s7a666"

line_len = len(line)

line_upper = sum(i.isupper() for i in line)

line_lower = sum(j.islower() for j in line)

line_special = 0

rek1 = "увеличить число символов - {}".format(12 - line_len)

rek2 = "добавить 1 заглавную букву"

rek3 = "добавить 1 цифру"

rek4 = "добавить 1 спецсимвол"

rek5 = "добавить 1 строчную букву"

er1 = "Ошибка. Запрещенный спецсимвол"

er2 = "Слабый пароль. Рекомендации: "

er0 = "Сильный пароль."


bad_s = "`~$][\"\'\\?.,:;|/"

for k in line:
    if k in bad_s:
        print(er1)
        break
else:
    s = "!@#$%^&*()-+"

    for i in range(0, line_len):
        if line[i] in s:
            line_special += 1

    line_digit = sum(k.isdigit() for k in line)

    # print(line_len, line_upper, line_lower, line_special, line_digit)

    if line_len > 11 and line_upper > 0 and line_lower > 0 and line_special > 0 and line_digit > 0:
        print(er0)

    elif line_len < 12 or line_upper < 1 or line_lower < 1 or line_special < 1 or line_digit < 1:
        print(er2)

        if line_len < 12:
            print(rek1)

        if line_upper < 1:
            print(rek2)

        if line_lower < 1:
            print(rek5)

        if line_special < 1:
            print(rek4)

        if line_digit < 1:
            print(rek3)