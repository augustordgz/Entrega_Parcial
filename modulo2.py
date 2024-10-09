def buscar_paciente(pacientes, num_historia):
    """
    Esta función busca en la matriz pacientes, un número de historia clínica ingresado por el usuario que coincida con otro guardado dentro de la matriz. En caso de coincidir devuelve la fila entera donde se encuentra ubicado ese número de historia clínica, en caso de no coincidir, devuelve None.
    
    Parametros =
    
    pacientes: Matriz donde se guarda la información de los pacientes.
    num_historia: Número de Historia Clínica del paciente que el usuario desea encontrar.
    """
    if not pacientes:
        print("La lista de pacientes está vacia.")
        return
    for paciente in pacientes:
        if paciente[0] == num_historia:
            return paciente
    return None

def ordenar_pacientes(pacientes):
    """
    Esta función utiliza el algoritmo de ordenamiento Bubble Sort para ordenar la matriz pacientes de forma ascendente, usando como referencia el número de Historia Clínica de cada paciente.
    
    Parametros =
    
    pacientes: Matriz donde se guarda la información de los pacientes.
    """
    if not pacientes:
        print("La lista de pacientes está vacia.")
        return
    for i in range (len(pacientes)):
        for j in range (0, len(pacientes) - i - 1):
            if pacientes[j][0] > pacientes [j + 1][0]:
                pacientes [j], pacientes[j + 1] = pacientes[j + 1], pacientes[j]
    print("Lista de pacientes ordenada por número de Historia Clínica de forma ascendente: ")
    for paciente in pacientes: 
        print(f"Número de Historia Clínica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnostico: {paciente[3]}, Días de internación: {paciente[4]}")
    return pacientes