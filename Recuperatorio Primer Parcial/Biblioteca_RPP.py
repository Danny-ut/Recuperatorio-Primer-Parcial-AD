estudiantes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [9, 8, 10],  # Ana
    [6, 7, 8],   # Bruno
    [10, 10, 9], # Carla
    [7, 6, 5]    # Diego
]

materias = ["Matemática", "Historia", "Biología"]

def mostrar_tabla() -> None:
    """
    Muestra una tabla con los nombres de los estudiantes y sus calificaciones.
    """
    print("Estudiantes y calificaciones:")
    for i in range(len(estudiantes)):
        print(estudiantes[i], "->", notas[i])

def calcular_promedios() -> list:
    """
    Calcula el promedio de cada estudiante en base a sus calificaciones.

    Retorno: Una lista de promedios, uno por cada estudiante.
    """
    promedios = []
    for fila in notas:
        suma = 0
        for nota in fila:
            suma += nota
        promedio = suma / 3
        promedios.append(promedio)
    return promedios

def ordenar_por_promedio() -> None:
    """
    Ordena las listas de estudiantes y calificaciones de mayor a menor según el promedio general.
    """
    print("\nOrdenando por promedio general...")
    promedios = calcular_promedios()
    for i in range(len(estudiantes) - 1):
        for j in range(i + 1, len(estudiantes)):
            if promedios[j] > promedios[i]:
                
                temp = estudiantes[i]
                estudiantes[i] = estudiantes[j]
                estudiantes[j] = temp
                
                temp_nota = notas[i]
                notas[i] = notas[j]
                notas[j] = temp_nota
                
                temp_prom = promedios[i]
                promedios[i] = promedios[j]
                promedios[j] = temp_prom

    print("Estudiantes ordenados por promedio:")
    for i in range(len(estudiantes)):
        print(estudiantes[i], "-> Promedio:", promedios[i], "->", notas[i])

def buscar_estudiante() -> None:
    """
    Pide al usuario el nombre de un estudiante y muestra sus calificaciones si lo encuentra.
    """
    nombre = input("\nIngresá el nombre de un estudiante para ver sus notas: ")
    encontrado = False
    for i in range(len(estudiantes)):
        if estudiantes[i] == nombre:
            print("Notas de", nombre + ":", notas[i])
            encontrado = True
    if not encontrado:
        print("Estudiante no encontrado.")

def es_entero(cadena: str) -> bool:
    """
    Verifica si una cadena representa un número entero positivo.

    Parametro: cadena: La cadena a verificar.

    Retorno: True si la cadena representa un número entero válido, False en caso contrario.
    """
    resultado = True
    if cadena == "":
        resultado = False
    for c in cadena:
        if c < "0" or c > "9":
            resultado = False
    return resultado

def buscar_calificacion() -> None:
    """
    Pide al usuario una calificación y muestra todos los estudiantes y materias donde aparece.
    """
    entrada = input("\nIngresá una nota para buscar su ubicación: ")
    if not es_entero(entrada):
        print("Debe ingresar un número entero.")
        return

    valor = int(entrada)
    encontrado = False
    for i in range(len(notas)):
        for j in range(len(notas[i])):
            if notas[i][j] == valor:
                print("Nota encontrada:", valor, "-> Estudiante:", estudiantes[i], ", Materia:", materias[j])
                encontrado = True
    if not encontrado:
        print("Esa nota no se encontró.")



