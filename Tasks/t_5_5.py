n = 9

for i in range(1, n + 1):  # left part

    for x in range(n - i, 0, -1):  # spaces
        print(" ", end="")

    for z in range(i, 0, -1):  # digits left
        print(z, end="")

    for j in range(2, i + 1):  # digits right
        print(j, end="")

    print("")


for i in range(n, 0, -1):  # left part

    for x in range(n - i, 0, -1):  # spaces
        print(" ", end="")

    for z in range(i, 0, -1):  # digits left
        print(z, end="")

    for j in range(2, i + 1):  # digits right
        print(j, end="")

    print("")
