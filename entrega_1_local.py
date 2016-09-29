import random
from simpleai.search import (SearchProblem, hill_climbing,
                             hill_climbing_random_restarts,
                             beam,
                             hill_climbing_stochastic,
                             simulated_annealing)
INICIAL = (
(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9),
(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9),
(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9),
)


def t2l(t):
    return list(t)
def l2t(l):
    return tuple(l)

class Hnefatafl(SearchProblem):

    def actions(self, state):
        acciones = []
        for guerrero in state:
            for fila in range(10):
                for columna in range(10):
                    if (fila, columna) not in state:
                        nuevaPos = fila, columna
                        acciones.append((guerrero, (nuevaPos)))

        return acciones

    def result(self, state, action):

        state = t2l(state)
        guerrero, nuevaPos = action
        state.remove(guerrero)
        state.append(nuevaPos)
        state = l2t(state)
        return state

    def value(self, state):
        puntaje = 0
        for i in range(10):
            for j in range(10):
                if (i, j) not in state:
                    ataque = 0
                    #arriba
                    if (i - 1, j) in state:
                        ataque = ataque + 1
                    #abajo
                    if (i + 1, j) in state:
                        ataque = ataque + 1
                    #derecha
                    if (i, j + 1) in state:
                        ataque = ataque + 1
                    #izquierda
                    if (i, j - 1) in state:
                        ataque = ataque + 1
                    #suma puntaje segun lo q sea

                    if ataque >= 2:
                        if i == 9 or j == 9 or i == 0 or j == 0:
                            puntaje = puntaje + 3
                        else:
                            puntaje = puntaje + 1

        return puntaje

    def generate_random_state(self):
        estado = []
        for i in range(30):
            bandera = 0
            while (bandera ==0):
                posible = (random.randint(0, 9) , random.randint(0, 9))
                if posible not in estado:
                    estado.append(posible)
                    bandera=1
        return tuple(estado)

def resolver(metodo_busqueda,iteraciones =200,haz= None, reinicios= None):
    problema= Hnefatafl(INICIAL)

    if metodo_busqueda == "hill_climbing":
        resultado= hill_climbing(problema,iteraciones)
        return resultado
    if metodo_busqueda == "hill_climbing_stochastic":
        resultado= hill_climbing_stochastic(problema,iteraciones)
        return resultado
    if metodo_busqueda == "beam":
        resultado= beam(problema,haz,iteraciones)
        return resultado
    if metodo_busqueda== "hill_climbing_random_restarts":
        resultado= hill_climbing_random_restarts(problema,reinicios,iteraciones)
        return resultado
    if metodo_busqueda== "simulated_annealing":
        resultado= simulated_annealing(problema,iterations_limit= iteraciones)
        return resultado

if __name__ == '__main__':

    problema = Hnefatafl(INICIAL)
    #Hill Climbing 200 iteraciones
    result = hill_climbing(problema, 200)

# es para imprimir el tablero
    print 'Estado:'
    for fila in range(10):
        for columna in range(10):
            if (fila, columna) in result.state:
                print '|*',
            else:
                print '| ',
        print
        print '-' * 30

    print 'Valor:'
    print result.value




