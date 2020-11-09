set1 = {1, 10, 223, 413, 2}
set2 = {1, 10, 223, 413, 2}

result = False

if set1 != set2:
    set1_len = len(set1)
    set2_len = len(set2)

    result = set1.issubset(set2)

print(result)

