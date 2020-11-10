from random import *

up_line = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d_line = '0123456789'
spec_line = '!@#$%^&*()-+'
new_pass = []
password = ""

print("enter length of the new password: ", end="")
len_pass = int(input())

if len_pass > 3:

    up_line_len = randint(3, len_pass // 2 + 2)

    d_line_len = randint(1, ((len_pass - up_line_len) // 3 + 2))

    spec_line_len = len_pass - up_line_len - d_line_len

    for up in range(up_line_len - 1):
        if up // 2 == 0:
            new_pass.extend(choice(up_line.lower()))
        else:
            new_pass.extend(choice(up_line))

    for spec in range(spec_line_len):
        new_pass.extend(choice(spec_line))

    for d in range(d_line_len):
        new_pass.extend(choice(d_line))

    new_pass = new_pass[:len_pass - 1]
    new_pass = new_pass[3:]

    new_pass.extend(choice(up_line.lower()))
    new_pass.extend(choice(up_line))
    new_pass.extend(choice(d_line))
    new_pass.extend(choice(spec_line))

    shuffle(new_pass)

    password = "".join(new_pass)

else:
    print("The password is too short (less than 4 chars)")

print(password)
