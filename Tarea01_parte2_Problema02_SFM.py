
import string

def contar_palabras(lista_palabras, ruta_fichero):
   
    # Inicializar diccionario con cero para cada palabra
    frecuencias = {palabra.lower(): 0 for palabra in lista_palabras}
    
    # Abrir y leer el fichero
    with open(ruta_fichero, 'r', encoding='utf-8') as fichero:
        for linea in fichero:
            # Eliminar puntuación y convertir a minúsculas
            linea = linea.translate(str.maketrans('', '', string.punctuation)).lower()
            palabras_linea = linea.split()
            
            # Contar las palabras
            for palabra in palabras_linea:
                if palabra in frecuencias:
                    frecuencias[palabra] += 1
    
    # Devolvemos el diccionario ordenado por palabra
    return dict(sorted(frecuencias.items()))

# ---  Programa  ---
if __name__ == "__main__":
    lista = ["cantar", "mayor", "un", "tiempo", "Señora", "jóvenes", "su", "Fortuna", "Elizabeth", "alba", "medianoche", 
             "negro", "Canal", "y", "fantasma", "madre", "joven"]
    ruta = "C:/Users/Usuario/Desktop/Tarea01PIA/texto.txt"  # Debe existir un fichero en la misma carpeta con el nombre indicado
    
    resultado = contar_palabras(lista, ruta)
    
    print("Frecuencia de palabras:")
    for palabra, freq in resultado.items():
        print(f"{palabra}: {freq}")







