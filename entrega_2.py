from simpleai.search import (CspProblem, backtrack,
                             MOST_CONSTRAINED_VARIABLE,
                             LEAST_CONSTRAINING_VALUE,
                             HIGHEST_DEGREE_VARIABLE,min_conflicts)

#min_conflicts,
slotsPares = (
    ('a','b'), ('a','c'),('b','d'),('c','d'),('d','f'),('c','e'),
    ('e','g'),('f','h'),('g','i'),('h','i'),('j','k'),('i','j'),('l','m'),
    ('k','l'),('l','n'),('l','p'),('p','o'),('p','q'))

slotsAdyacentes = (
    ('a','b', 'c'), ('b','a', 'd'), ('c', 'e', 'a', 'd'), ('d', 'b', 'f', 'c'), ('e','c', 'g'),
    ('f', 'h', 'd'), ('g', 'e', 'h', 'i'), ('h', 'f', 'g', 'i'), ('i', 'j', 'g', 'h'), ('j', 'i', 'k'),
    ('k', 'j', 'l'), ('l' ,'k', 'm', 'n', 'p'), ('m', 'l'), ('n', 'l'), ('o', 'p'), ('p', 'l', 'o', 'q'),
    ('q', 'p'))

slots = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
         'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q')

modulos = ['Lasers', 'Motores', 'Cabinasparatripulantes',
           'Bahiasdecarga', 'Sistemasdevidaextraterrestre',
           'Escudos', 'Baterias']


dominios = {slot: ['Lasers', 'Motores', 'Cabinasparatripulantes',
                   'Bahiasdecarga', 'Sistemasdevidaextraterrestre',
                   'Escudos', 'Baterias']
           for slot in slots}


#########################################################################

def motorLugares(variables, values):
    #posiciones del motor
    if('Motores') in values:
        return variables[values.index('Motores')] in('o', 'p', 'q', 'm', 'n', 'e', 'f')
    return True

def LaserBateria(variables,values):
    #laser no tiene q estar cerca de la bateria
    sloat_a, sloat_b= values

    if sloat_a == 'Lasers' and sloat_b =='Baterias'or sloat_a =='Baterias' and sloat_b== 'Lasers':
                return False
    return True

def CabinaMotores(variables,values):
    #cabina no conectada a los motores
    sloat_a, sloat_b= values

    if sloat_a == 'Cabinasparatripulantes' and sloat_b =='Motores'or sloat_a =='Motores' and sloat_b== 'Cabinasparatripulantes':
                return False
    return True

def escudoExtraterrestre(variables,values):
    #escudo no conectados a sistema de vida extraterrestres
    if 'Escudos'not in values or 'Sistemasdevidaextraterrestre' not in values:
        return True

def distintos(variables,values):
    sloat_a, sloat_b = values
    #no debe haber dos seguidos
    return sloat_a != sloat_b


def extraterrestreCabina(variables, values):
     #sistema de extraterrestre conectado a la cabina
    if 'Cabinasparatripulantes' in values and 'Sistemasdevidaextraterrestre' in values:
                return True
    return False

def bahiasCabina(variables, values):
    if 'Bahiasdecarga' == values[0]:
        return 'Cabinasparatripulantes' in values
    return True

def bateriaDosElementos(variables, values):

    #mas q dos conexiones a la bateria
    if values[0] == 'Baterias':
        cant = 0
        for variable in values:
            if variable == 'Lasers':
                cant = cant + 1
            if variable == 'CabinasTripulantes':
                cant = cant + 1
            if variable == 'Escudos':
                cant = cant + 1
            if variable == 'SistemasVidaExtraterrestre':
                cant = cant + 1
        if cant > 1:
            return true

def TodosModulos(variables,values):
    for m in modulos:
        if m not in values:
            return False
    return True

#########################################################################
restricciones = []

restricciones.append((slots,TodosModulos))


for slot in slotsPares:
    restricciones.append((slot, LaserBateria))
    restricciones.append((slot, CabinaMotores))
    restricciones.append((slot, escudoExtraterrestre))
    restricciones.append((slot, distintos))

for slot in slotsAdyacentes:
    restricciones.append((slotsAdyacentes, extraterrestreCabina))
    restricciones.append((slotsAdyacentes, bahiasCabina))
    restricciones.append((slotsAdyacentes, bateriaDosElementos))
    restricciones.append((slot,motorLugares))


if __name__ == '__main__':
    problema = CspProblem(slots, dominios, restricciones)

    resultado = backtrack(problema)
    print resultado

    resultado = min_conflicts(problema, iterations_limit=500)
    print resultado





