list = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']

list_len = len(list)

result = {i: list.count(i) for i in list}
print(result)

"""for j in list:
    c = list.count(j)
    print(c)"""

for k in result.values():
    print(k, end=", ")
