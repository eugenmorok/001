list = [-5, 5, 10]

list_max = max(list)
list_min = min(list)

idx_max = list.index(list_max)
idx_min = list.index(list_min)

list.pop(idx_min)
list.insert(idx_min, list_max)
list.pop(idx_max)
list.insert(idx_max, list_min)

print(list)
