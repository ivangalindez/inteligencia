from simpleai.search import astar, SearchProblem,breadth_first,depth_first,greedy
from simpleai.search.viewers import BaseViewer

guerreros = (
    (0,0),(0,2),(0,4),(0,6),
    (1,4),
    (2,0),
    (3,1),(3,6),(3,7),(3,9),
    (4,0),(4,7),(4,8),
    (5,4),(5,9),
    (6,0),(6,5),(6,9),
    (7,0),(7,7),
    (8,2),(8,4),(8,9),
    (9,1),(9,4),(9,6),(9,7)
    )


rey=(5,3)

RangoMax=9
RangoMin=0


def t2l(t):
    return list(t)
def l2t(l):
    return tuple(l)

class Hnefatafl(SearchProblem):
    def cost(self, state1, action, state2):
        return 1

    def is_goal(self, state):
        if state[0] == 9 or state[1] == 9:
            return state
        if state[0] == 0 or state[1] == 0:
            return state


    def actions(self, state):
        acciones = []
        Reyx= state[0]
        Reyy= state[1]


        Mov=[(Reyx+ 1 , Reyy), (Reyx-1 , Reyy), (Reyx, Reyy+1), (Reyx , Reyy-1)]
        #abajo,arriba,derecha,izquierda

        #abajo
        if Mov[0] not in guerreros:
            #if Mov[0][0]+1 <=9:
                ataque=0
                if (Mov[0][0]+1 , Mov[0][1]) in guerreros:
                    ataque=ataque+1
                if ( Mov[0][0] , Mov[0][1]+1) in guerreros:
                    ataque=ataque+1
                if ( Mov[0][0] , Mov[0][1]-1) in guerreros:
                    ataque=ataque+1
                if ataque <=1:
                    acciones.append(Mov[0])

        #arriba
        if Mov[1] not in guerreros:
                ataque=0
            #if Mov[1][0]-1 >=0:
                if (Mov[1][0]-1 , Mov[1][1]) in guerreros:
                    ataque=ataque+1
                if ( Mov[1][0] , Mov[1][1]+1) in guerreros:
                    ataque=ataque+1
                if ( Mov[1][0] , Mov[1][1]-1) in guerreros:
                    ataque=ataque+1
                if ataque <=1:
                    acciones.append(Mov[1])
        #derecha
        if Mov[2] not in guerreros:
                ataque=0
            #if Mov[2][1]+1<=9:
                if (Mov[2][0],Mov[2][1]+1) in guerreros:
                    ataque=ataque+1
                if (Mov[2][0]+1,Mov[2][1]) in guerreros:
                    ataque=ataque+1
                if (Mov[2][0]-1,Mov[2][1]) in guerreros:
                    ataque=ataque+1
                if ataque<=1:
                    acciones.append(Mov[2])
        #izquierda
        if Mov[3] not in guerreros:
                ataque=0
            #if Mov[3][1]+1>=0:
                if (Mov[3][0],Mov[3][1]-1) in guerreros:
                    ataque=ataque+1
                if (Mov[3][0]+1,Mov[3][1]) in guerreros:
                    ataque=ataque+1
                if (Mov[3][0]-1,Mov[3][1]) in guerreros:
                    ataque=ataque+1
                if ataque<=1:
                    acciones.append(Mov[3])
        return acciones


    def result(self, state, action):

        state1= t2l(state)
        state1= action
        state=l2t(state1)

        return state

    def heuristic(self,state):
        Reyx= state[0]
        Reyy= state[1]

        if Reyx >= 5:
            return min(Reyy, 9-Reyx)
        else:
            return max(Reyx, 9-Reyy)

def resolver(metodo_busqueda, posicion_rey, controlar_estados_repetidos):
    problema= Hnefatafl(posicion_rey)

    if metodo_busqueda == "breadth_first":
        resultado= breadth_first(problema,graph_search= controlar_estados_repetidos)
        return resultado
    if metodo_busqueda == "depth_first":
        resultado= depth_first(problema,graph_search= controlar_estados_repetidos)
        return resultado
    if metodo_busqueda == "greedy":
        resultado= greedy(problema,graph_search= controlar_estados_repetidos)
        return resultado
    if metodo_busqueda== "astar":
        resultado= astar(problema,graph_search= controlar_estados_repetidos)
        return resultado


#graph_search=True

if __name__ == '__main__':
    problema = Hnefatafl(rey)

    #Estrella Arbol
    resultado = astar(problema,BaseViewer())
    resultado = astar(problema)

    #Estrella Grafo
    #resultado = astar(problema,graph_search=True,viewer=WebViewer())
    #resultado = astar(problema)

    print "Estado meta:"
    print resultado.state
    print "Camino:"
    for accion, estado in resultado.path():
        print "Movi", accion
        print "Llegue a", estado

