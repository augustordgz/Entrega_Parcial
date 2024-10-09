def contar_dias_internacion(pacientes):
    """
    Esta función cuenta la cantidad de pacientes con una cantidad de días de internación mayor a 5, luego muestra por pantalla la cantidad de pacientes que poseen más de 5 días de internación.
    
    Parametros =
    
    pacientes: Matriz donde se guarda la información de los pacientes.
    """
    if not pacientes:
        print("La lista de pacientes está vacia.")
        return
    contador = 0
    for paciente in pacientes:
        if paciente[4] > 5:
            contador += 1
    print(f"La cantidad de pacientes con más de 5 dias de internación son: {contador}")

def promediar_dias_internacion(pacientes):
    """
    Esta función suma la cantidad de pacientes ingresados a la matriz pacientes y los guarda en la variable 'contador_pacientes', y suma la cantidad de días de internación de cada uno en la variable 'contador_dias'. Luego divide la suma de la cantidad de pacientes ingresador por la suma de la cantidad de días de internación de todos los pacientes ingresados, para al final mostrarlo por pantalla.
    
    Parametros =
    
    pacientes: Matriz donde se guarda la información de los pacientes.
    """
    if not pacientes:
        print("La lista de pacientes está vacia.")
        return
    contador_dias = 0
    contador_pacientes = 0
    for paciente in pacientes:
        if paciente[4] > 0:
            contador_pacientes += 1
            contador_dias += paciente[4]
    promedio_dias = contador_dias / contador_pacientes
    print(f"El promedio de días de internación de todos los pacientes es: {promedio_dias}")