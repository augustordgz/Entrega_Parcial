def mostrar_max(pacientes):
    """
    Esta funcion compara la cantidad de días de internación de cada uno de los pacientes guardados en la matriz pacientes, luego de comparar, guarda el nombre del paciente con la mayor cantidad de días de internacion en la variable 'max_paciente' para luego mostrarlo por pantalla.
    
    Parametros =
    
    pacientes: Matriz donde se guarda la información de los pacientes.
    """
    if not pacientes:
        print("La lista de pacientes está vacia.")
        return
    max_paciente = pacientes[1]
    for paciente in pacientes:
        if paciente[4] > max_paciente[4]:
            max_paciente = paciente
    print (f"El paciente con más días de internación es: {max_paciente}")

def mostrar_min(pacientes):
    """
    Esta funcion compara la cantidad de días de internación de cada uno de los pacientes guardados en la matriz pacientes, luego de comparar, guarda el nombre del paciente con la menor cantidad de días de internacion en la variable 'min_paciente' para luego mostrarlo por pantalla.
    
    Parametros =
    
    pacientes: Matriz donde se guarda la información de los pacientes.
    """
    if not pacientes:
        print("La lista de pacientes está vacia.")
        return
    min_paciente = pacientes[1]
    for paciente in pacientes: 
        if paciente[4] < min_paciente[4]:
            min_paciente = paciente
    print(f"El paciente con menos días de internación es: {min_paciente}")