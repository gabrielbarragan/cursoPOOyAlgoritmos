import random

def busqueda_lineal(list, objetivo):
    match= False
    for elemento in list:
        if elemento == objetivo:
            match = True
            break
    return match

if __name__== '__main__':
    size_list = int(input('Indica el tamaño de la lista:\n'))
    objetivo = int(input('Por favor indica el número que quieres encontrar:\n'))
    lista= [random.randint(0,100) for i in range (size_list)]
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} En la lista')