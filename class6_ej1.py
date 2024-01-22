'''
import os
resp = 1
while resp != 0:
    print("Paint (1)")
    print("Calc (2)")
    print("Apagar PC en 2 horas (3)")
    print("Salir (0)")
    resp = int(input("Seleccione: "))
    if(resp == 1):
        os.system("mspaint")
    elif(resp == 2):
        os.system("calc")
    elif(resp == 3):
        os.system("shutdown -s -t 7200")
    else:
        print("No entiendo esa orden")
'''

import os
resp = 1
while resp != 0:
    print("Lana del Rey - West Coast")
    resp = int(input("Elija: "))

    if (resp == 1):
        os.system("start chrome www.youtube.com/watch?v=oKxuiw3iMBE")
    else:
        print(":(")