import time

estado_actual = ["verde" , "amarillo" , "rojo"]

def cambiar_semaforo(estado_actual):
    for estado in estado_actual:
            esperar(estado)
    print("Fin de ciclo")        
        
def esperar (estado):
    if estado == "verde":
        print("El semaforo esta en verde, cambiando a amarillo en 5 segundos")
        time.sleep(5)
    elif estado == "amarillo":
        print("El semaforo esta en amarillo, cambiando a rojo en 2 segundos")
        time.sleep(2)
    elif estado == "rojo":
        print("El semaforo esta en rojo, cambiando a amarillo en 3 segundos")
        time.sleep(3)   

print("Inciando la Simulacion")

for ciclo in range(3):
    cambiar_semaforo(estado_actual)
    iteracion_actual = 2 - ciclo
    print(f"Quedan {iteracion_actual} ciclos")
    