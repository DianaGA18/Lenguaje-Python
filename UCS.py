# Viaje por Carretera con Busqueda de costo Uniforme
import functools
from BFS import Nodo

# x es el coste y y es el nodo de salida
def compara(x, y):
    return x.get_coste() - y.get_coste()

def buscar_solucion_UCS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_coste(0)
    nodos_frontera.append(nodo_inicial)
    while (not solucionado) and len(nodos_frontera) != 0:
        # Ordenar la lista de nodos_frontera
        # Regresa una lista ordenada de orden ascendente
        nodos_frontera = sorted(nodos_frontera, key = functools.cmp_to_key(compara))
        nodo = nodos_frontera[0]
        # Extraer Nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
            # Solucion Encontrada
            solucionado = True
            return nodo
        else:
            # Expandir nodos hijo (Ciudades con conexiones)
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                coste = conexiones[dato_nodo][un_hijo]
                hijo.set_coste(nodo.get_coste() + coste)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados):
                    # Si esta en la lista, lo sustituimos con el nuevo valor del coste si es menor
                    if hijo.en_lista(nodos_frontera):
                        for n in nodos_frontera:
                            if n.igual(hijo) and n.get_coste() > hijo.get_coste():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)
                nodo.set_hijos(lista_hijos)

if __name__ == '__main__':
    conexiones = {
        'Jilotepec' : {'Michoacan' : 125, 'Morelia' : 513},
        'Zacatecas' : {'Morelia' : 514},
        'Michoacan' : {'Jilotepec' : 125, 'Morelia' : 423, 'Monterrey' : 491},
        'Monterrey' : {'Michoacan' :491, 'Morelia' : 355, 'Nayarit' : 309, 'Guadalajara' : 346},
        'Morelia' : {'CDMX' : 203, 'Zacatecas' : 514, 'Jilotepec' : 513, 'Michoacan' : 423, 'Guadalajara' : 603, 'San Luis Potosi' : 437, 'Monterrey' : 355, 'Nayarit' : 313, 'San Luis Potosi' : 437, 'Pachuca' : 599},
        'CDMX' : {'Pachuca' : 390, 'Morelia' : 203},
        'Pachuca' : {'CDMX' : 390, 'Morelia' : 599},
        'San Luis Potosi' : {'Morelia' :437, 'Nayarit' : 394},
        'Nayarit' : {'Guadalajara' : 296, 'Monterrey' : 309, 'Morelia' : 313},
        'Guadalajara' : {'Nayarit' : 296, 'Morelia' : 603, 'Monterrey' : 346}
    }

    estado_inicial = 'Jilotepec'
    solucion = 'Pachuca'
    nodo_solucion = buscar_solucion_UCS(conexiones, estado_inicial, solucion)

    # Mostrar Resultados
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    print('Costo: ' + str(nodo_solucion.get_coste()))

    # Jilotepec, Morelia, CDMX, Pachuca
    # 1106km