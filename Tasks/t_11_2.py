dict = {'Hello' : 'Hi', 'Bye' : 'Goodbye', 'List' : 'Array'}

val_in = input()

for k, v in dict.items():
    if v == (val_in):
        print(k)
