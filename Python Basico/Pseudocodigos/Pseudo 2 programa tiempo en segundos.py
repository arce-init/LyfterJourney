tiempo = float(input("Introduzca su tiempo en segundos: "))
falta = 0
if tiempo < 600:
    falta = 600 - tiempo
    print(f"Faltan {falta} segundos")
elif tiempo > 600:
    print("Mayor")
else:
    print("Igual")