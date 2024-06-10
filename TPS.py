# Vuelos con Busqueda en Amplitud

from BFS import Nodo

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodos_frontera.append(nodo_inicial) # Si no esta, lo insertamos en nodos frontera
    while(not solucionado and len(nodos_frontera) != 0):
        nodo = nodos_frontera[0] # Se empuja el resto de los nodos
        # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
            # Solucion encontrada
            solucionado = True
            return nodo
        else:
            # Expandir nodos hijo (ciudades con conexion)
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)
    
if __name__ == '__main__':
    conexiones = {
        'Jilotepec' : {'CDMX', 'Morelia', 'Guadalajara'},
        'Zacatecas' : {'Pachuca', 'Morelia'},
        'Puebla' : {'Michoacan'},
        'Michoacan' : {'Guadalajara'},
        'Morelia' : {'CDMX', 'Zacatecas', 'Jilotepec', 'Guadalajara', 'San Luis Potosi'},
        'CDMX' : {'Jilotepec', 'Morelia'},
        'Pachuca' : {'Zacatecas', 'San Luis Potosi', 'Guadalajara'},
        'San Luis Potosi' : {'Pachuca', 'Morelia'},
        'Nayarit' : {'Guadalajara'},
        'Guadalajara' : {'Nayarit', 'Pachuca', 'Morelia', 'Sonora', 'Michoacan'}
    }

estado_inicial = 'Jilotepec'
solucion = 'Pachuca'
nodo_solucion = buscar_solucion_BFS(conexiones, estado_inicial, solucion)

# Mostrar Resultado
resultado = []
nodo = nodo_solucion
# Recorrer Arbol
while nodo.get_padre() != None:
    resultado.append(nodo.get_datos())
    nodo = nodo.get_padre()
resultado.append(estado_inicial)
resultado.reverse()
print(resultado)