
    #Listas iniciales de números enteros
lista1 = [1, -2, 33, 14, -5, 0, 20, 3, -10, 22, 4, 2, 81, 102, 29]
lista2 = [4, 50, 2, 29, 16, 7, 81, 0, -2, 3, 33, -10, 20, 1, 93, 100, -34, -77]

def analizar_listas(lista1, lista2):
    
        # Convertir listas a conjuntos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
        # Calcular intersección, unión y diferencia simétrica
    interseccion = conjunto1 & conjunto2            # o conjunto1.intersection(conjunto2)
    union = conjunto1 | conjunto2                  # o conjunto1.union(conjunto2)
    diferencia_simetrica = conjunto1 ^ conjunto2   # o conjunto1.symmetric_difference(conjunto2)
    
        # Devolver resultados en un diccionario
    resultado1 = {
        "interseccion": interseccion,
        "union": union,
        "diferencia_simetrica": diferencia_simetrica
    }
    
    return resultado1

resultado1 = analizar_listas(lista1, lista2)
print(resultado1)





