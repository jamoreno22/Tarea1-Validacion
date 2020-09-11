import sys
from datetime import datetime as dt
def comparador(a,b):
    a = str(a)
    b = str(b)
    if len(a) < len(b):
        f.write("\nFecha:" + str(dt.now()) + "\nCadena 1:"+ a + "\nCadena 2:"+ b + "\nCadena más larga:" + b)
        print("La cadena", b, "es más larga")
    elif len(a) > len(b):
        f.write("\nFecha:" + str(dt.now()) + "\nCadena 1:"+ a + "\nCadena 2:"+ b + "\nCadena más larga:" + a)
        print("La cadena", a, "es más larga")
    else:
        f.write("\nFecha:"+ str(dt.now()) + "\nCadena 1:"+ a + "\nCadena 2:"+ b + "\nCadena más larga: Ambas son iguales")
        print("Ambas cadenas tienen el mismo largo")
    return

f = open("logs.txt","a")

if len(sys.argv)==3:
    a,b = sys.argv[1], sys.argv[2]
    comparador(a,b)
else:
    f.write("\nFecha:" + str(dt.now()) + "\nError, cantidad incorrecta de strings")
    print("numero de cadenas incorrecto")