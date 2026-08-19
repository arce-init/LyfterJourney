def print_all_pairs(my_dict):
    for key1 in my_dict:
        for key2 in my_dict:
            print(f"{key1}-{key2}")
#O(n²) — dos ciclos anidados, ambos recorriendo el mismo diccionario
#(n = cantidad de claves). Por cada clave del ciclo externo, se
#recorren TODAS las claves del ciclo interno.