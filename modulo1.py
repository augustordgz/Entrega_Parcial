def cargar_pacientes(pacientes):
    """
    Esta función permite ingresar la cantidad de pacientes que el usuario desee a la matriz de pacientes. Nos solicita una cantidad de pacientes determinada a ingresar, número de historia clínica, nombre, edad, diagnostico y días de internación de cada uno de los pacientes.
    
    Parametros =
    
    pacientes: Matriz donde se ingresa la información de los pacientes.
    """
    cantidad = int(input("Ingrese la cantidad de pacientes a cargar: "))
    for _ in range(cantidad):
        num_historia = int(input("Ingrese el número de historia clínica: "))
        nombre_paciente = str(input("Ingrese el nombre del paciente: "))
        edad_paciente = int(input("Ingrese la edad del paciente: "))
        diagnostico = str(input("Ingrese el diagnostico: "))
        dias_internacion = int(input("Ingrese la cantidad de días de internación: "))
        pacientes.append([num_historia, nombre_paciente, edad_paciente, diagnostico, dias_internacion])

def mostrar_lista_pacientes(pacientes):
    """
    Esta funcion imprime por línea cada fila de la matriz pacientes, cada fila corresponde a la información de un paciente.
    
    Parametros =
    
    pacientes: Matriz donde se guarda la información de los pacientes.
    """
    if not pacientes:
        print("La lista de pacientes está vacia.")
        return
    for i in range(len(pacientes)):
        print(pacientes[i])