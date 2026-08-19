def manual_add(n):
    result = 0
    for i in range(1, n + 1):    # <- era "number", pero el parámetro se llama "n"
        result += i
    return result

#O(n) — un solo ciclo que se ejecuta n veces, sumando uno por uno.


def add_formula(n):
    return n * (n + 1) // 2       # <- mismo problema, "number" no existe

#O(1) — no hay ningún ciclo. Es una fórmula matemática directa
#(la fórmula de Gauss) que calcula el resultado en un solo paso,
#sin importar qué tan grande sea n.