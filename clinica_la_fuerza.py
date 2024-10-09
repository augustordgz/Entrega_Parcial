from modulo1 import *
from modulo2 import *
from modulo3 import *
from modulo4 import *

def menu():
    menu_lista = """
    --- Sistema de Gestión de Clínica ---
    1. Cargar pacientes.
    2. Mostrar todos los pacientes.
    3. Buscar pacientes por número de Historia Clínica.
    4. Ordenar pacientes por número de Historia Clínica.
    5. Mostrar paciente con más días de internación.
    6. Mostrar paciente con menos días de internación.
    7. Cantidad de pacientes con más de 5 dias de internación.
    8. Promedio de días de internacion de todos los pacientes.
    9. Salir.
    """
    pacientes = []
    salir = ""
    while salir != "salir":
        print(menu_lista)
        opcion = input("Seleccione una opcion: ")
        if opcion == '1':
            paciente = cargar_pacientes(pacientes)
        elif opcion == '2':
            mostrar_lista_pacientes(pacientes)
        elif opcion == '3':
            buscar_num_historia = int(input("Ingrese el número de Historia Clínica a buscar: "))
            paciente = buscar_paciente(pacientes, buscar_num_historia)
            if paciente:
                print(f"Paciente encontrado: {paciente}")
            else:
                print("Paciente no encontrado.")
        elif opcion == '4': 
            pacientes = ordenar_pacientes(pacientes) 
        elif opcion == '5':
            mostrar_max(pacientes)
        elif opcion == '6':
            mostrar_min(pacientes)
        elif opcion == '7':
            contar_dias_internacion(pacientes)
        elif opcion == '8':
            promediar_dias_internacion(pacientes)
        elif opcion == '9':
            print("Saliendo del sistema...")
            salir = "salir"
        else:
            print("Opcion no valida. Por favor, intente de nuevo.")

menu()