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

line = "@PowerRangers123@"

line_len = len(line)

line_upper = sum(i.isupper() for i in line)

line_lower = sum(j.islower() for j in line)

line_special = 0
s = "(.,:;!_*-+()/#¤%&@)"
for i in range(0, line_len):
    if line[i] in s:
        line_special += 1

line_digit = sum(k.isdigit() for k in line)

#print(line_len, line_upper, line_lower, line_special, line_digit)

rek1 = "увеличить число символов - {}".format(12 - line_len)

rek2 = "добавить 1 заглавную букву"

rek3 = "добавить 1 цифру"

rek4 = "добавить 1 спецсимвол"

rek5 = "добавить 1 строчную букву"

er1 = "Ошибка. Запрещенный спецсимвол"

er2 = "Слабый пароль. Рекомендации: "

er0 = "Сильный пароль."

if line_len > 11 and line_upper > 0 and line_lower > 0 and line_special > 0 and line_digit > 0:
    print(er0)
elif line_upper > 0 and line_lower > 0 and line_special > 0 and line_digit > 0:
    print(er2 + rek1)
elif line_len > 11 and line_lower > 0 and line_special > 0 and line_digit > 0:
    print(er2 + rek2)
elif line_len > 11 and line_upper > 0 and line_special > 0 and line_digit > 0:
    print(er2 + rek5)
elif line_len > 11 and line_upper > 0 and line_lower > 0 and line_digit > 0:
    print(er2 + )
