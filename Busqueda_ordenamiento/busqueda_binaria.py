import random

def busqueda_binaria (list, start, end, target, contador=1):
    print(f'Buscando el {target} entre {list[start]} y {list[end-1]}. iteración: {contador}')
    if start > end:
        return False
    mid= (start + end) // 2
    if list[mid] == target:
        return True
    elif list[mid] < target:
        contador+=1
        return busqueda_binaria(list, mid+1, end, target, contador)
    elif list[mid] > target:
        contador+=1
        return busqueda_binaria(list, start, mid-1, target, contador)


if __name__== '__main__':
    size_list = int(input('Indica el tamaño de la lista:\n'))
    objetivo = int(input('Por favor indica el número que quieres encontrar:\n'))
    lista= sorted([random.randint(0,100) for i in range (size_list)])
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} En la lista')