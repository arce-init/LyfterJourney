def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1   # <- era "lst", pero el parámetro se llama "my_list"
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

#O(n) — en el peor caso (el elemento no está, o está al final),
#hay que recorrer toda la lista un elemento a la vez.

def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
#O(log n) — en cada vuelta del while, se descarta la MITAD de los
#elementos restantes, así que el rango de búsqueda se reduce
#exponencialmente rápido en vez de ir de uno en uno.