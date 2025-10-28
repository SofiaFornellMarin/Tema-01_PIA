
    # Lista inicial de números enteros.
listaInicial = [10, 8, -9, 3, 1, -3, 7, 8, 5, 13, 0, 9, 7, 3]
listaFinal = []
positivos = []
unicos = []

print("Lista de números enteros inicial:")
print(listaInicial)
print("----------------------------------------")


def eliminar_negativos(lista):
    lista01 = []
    for elemento in lista:
        if elemento >= 0:   # Solo añadimos los números no negativos
            lista01.append(elemento)
            
        # Mostramos la lista de los positivos obtenida.
    print("Lista de números positivos:")
    print(lista01)
    print("----------------------------------------")
    return lista01

def eliminar_duplicados(lista):
    lista02 = []
    for numero in lista:
        if numero not in lista02:
            lista02.append(numero)
            
        # Mostramos la lista de los positivos obtenida.
    print("Lista de números sin duplicaciones:")
    print(lista02)
    print("----------------------------------------")
    return lista02

    # Llamamos a las dos primeras funciones:
positivos = eliminar_negativos(listaInicial)
unicos = eliminar_duplicados(positivos)

    # Ordenamos la lista sin duplicados usando sorted() que no modifica la lista original
ordenada = sorted(unicos)
listaFinal = ordenada

    # Mostramos la lista final que se solicita en el enunciado.
print("******************************************************************************************")
print("*************************** RESULTADO FINAL **********************************************")
print("* Lista de números enteros positivos sin repeticiones y ordenados de menor a mayor: ")
print("* ", listaFinal)
print("******************************************************************************************")


