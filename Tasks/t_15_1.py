def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails


f = open('task_file.txt', 'r')

lines = []
names = []

for line in f:
    s = line.replace(',', '').split()
    if len(s) > 3 and len(s[2]) == 7 and (s[0] or s[1] or s[2] or s[3]) != 'NO_NAME'\
            and (s[0][0].isupper() and s[1][0].isupper() and s[3][0].isupper())\
            and s[3] != 'LAST_NAME':
        #print(s)
        lines.append(s)
        names.append(s[0:2])
f.close()

#print(lines)
#print(names)

emails = email_gen(names)

#print(emails)

template = 'EMAIL, NAME, LAST_NAME, TEL, CITY, '

for i in range(len(lines)):
    lines[i].insert(0, emails[i])

for item in lines:
    template = template + ", ".join(item) + ", "

#print(template)

nf = open('task_file.txt', 'w')
nf.write(template)

nf.close()









