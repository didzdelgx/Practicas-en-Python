for x in range(5):
    print("* " * 5)

for x in range(5):
    print("* " * (x+1))

for x in range(5):
    if x == 0 or x == 4:
        print("* " * 5)
    else:
        print("*         *")
# solo boders?
tablero = [
    ['h','o','l','a','s'],
    ['s','l','i','m','e'],
    ['a','i','r','a','m'],
    ['o','s','m','a','l'],
    ['l','u','c','h','i'],
    ]
fila = 5
columna = 5 