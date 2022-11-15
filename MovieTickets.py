import heapq

 tiquetsvendi = 0
 retornA= 0
# Funcion para recolectar la maxima cantidad de tiquetes  
def cantidadMaxima(i, j, puestos):
    # cuento asientos vacios
    cont = puestos
    heapq._heapify_max(cont)
    # #de tiquetes vendidos
    while tiquetsvendi < j and cont[0] > 0:
        
        retornA = retornA+ cont[0]
        cont[0] -= 1
        if cont[0] == 0:
            break
            
        heapq._heapify_max(cont)
        tiquetsvendi = tiquetsvendi+ 1
    return retornA
 
puestos = [1, 2, 4]
i = len(puestos)
j = 3
print(cantidadMaxima(i, j, puestos))
