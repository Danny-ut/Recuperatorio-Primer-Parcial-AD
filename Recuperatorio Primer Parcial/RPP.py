from Biblioteca_RPP import *

def main():
    """Muestra un menú interactivo para que el usuario acceda a las distintas funcionalidades del sistema."""
    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Mostrar estudiantes y calificaciones")
        print("2. Ordenar por promedio (mayor a menor)")
        print("3. Buscar estudiante por nombre")
        print("4. Buscar calificación")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_tabla()
        elif opcion == "2":
            ordenar_por_promedio()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            buscar_calificacion()
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.")

main()
"""Ejecucion del programa"""