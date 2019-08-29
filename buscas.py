import os
import numpy as np

list = [2, 8, 10, 13, 23, 27, 34, 41, 49, 50]
biglist = [  9,  11,  15,  25,  32,  34,  35,  47,  53,  57,  59,  66,  68,  69,  86,  92,  94,  98,
 105, 108, 112, 120, 131, 132, 135, 137, 138, 142, 143, 143, 146, 168, 169, 169, 171, 172,
 177, 178, 178, 191, 193, 195, 195, 197, 199, 205, 209, 209, 222, 224, 228, 229, 233, 234,
 238, 239, 247, 248, 254, 257, 262, 266, 274, 279, 289, 299, 313, 333, 335, 338, 362, 365,
 367, 369, 378, 379, 379, 385, 385, 397, 398, 401, 401, 406, 446, 453, 455, 462, 466, 469,
 472, 476, 478, 479, 481, 482, 487, 493, 499, 500, 513, 513, 518, 519, 528, 528, 539, 539,
 540, 543, 544, 550, 551, 555, 558, 558, 561, 563, 568, 581, 585, 588, 593, 598, 599, 603,
 618, 619, 627, 634, 634, 639, 641, 642, 653, 657, 658, 659, 659, 660, 661, 673, 683, 696,
 697, 701, 703, 706, 706, 706, 707, 739, 748, 754, 754, 757, 758, 762, 776, 787, 789, 792,
 795, 796, 799, 802, 803, 805, 808, 808, 809, 815, 821, 824, 848, 863, 875, 878, 893, 897,
 899, 905, 908, 910, 917, 919, 931, 933, 933, 934, 934, 934, 962, 963, 971, 972, 983, 992,
 997, 998]


def printa_negrito(lista):
    for element in lista:
        for other_element in lista:
            if (element == other_element):
                print('\033[1m' + str(other_element) + '\033[0m', end = " ")
            else:
                print(str(other_element), end = " ")
        print('\n')
    return

# Esse método não altera a lista utilizada
def busca_sequencial(lista, alvo):
    tamanho = len(lista)
    for registro in lista:
        if(registro == alvo):
            return lista.index(alvo)
    else:
        return(-1)

# Esse método altera a lista que é passada como parâmetro
def busca_sequencial_sentinela(lista, alvo):
    lista.append(alvo)
    tamanho = len(lista)
    for aux in range(tamanho):
        if(lista[aux] == alvo):
            break
    if(aux < tamanho - 1):
        return aux
    else:
        return(-1)

# Método para criar index da lista, primeiro com a lista e depois com a quantidade de elementos que terão no index
def cria_index(lista, numeros_index):
    tamanho = len(lista)
    escala = tamanho//numeros_index
    index = []
    for elemento in range(0, tamanho-1, escala):
        index.append((elemento, lista[elemento])) # Cria tupla com o a posição do elemento na lista e o elemento
    return index

# Método de busca sequencial indexada
def busca_sequencial_indexada(index, lista, alvo):
    tamIndex = len(index)
    tamLista = len(lista)
    for elemento in range(tamIndex):
        if(elemento == tamIndex - 1):
            for inElemento in range(elemento, tamLista-1, 1):
                if(lista[inElemento] == alvo):
                    return inElemento
            else:
                return(-1)
        else:
            if( (index[elemento][1] <= alvo) and (index[elemento+1][1] >= alvo) ):
                for inElemento in range(index[elemento][0], index[elemento+1][0], 1):
                    if(lista[inElemento] == alvo):
                        return inElemento
                else:
                    return(-1)

# Recursiva sim, foda-se
def busca_binaria(lista, alvo, auxPos):
    print(lista)
    tamanho = len(lista)
    pos = (tamanho//2)
    novaLista = []
    if(lista[pos] == alvo):
        if(auxPos > -1):
            return pos + auxPos
        else:
            return pos
    elif(lista[pos] > alvo):
        for elemento in range(pos):
            novaLista.append(lista[elemento])
        return busca_binaria(novaLista, alvo, auxPos)
    elif(lista[pos] < alvo):
        for elemento in range(pos, tamanho, 1):
            novaLista.append(lista[elemento])
        return busca_binaria(novaLista, alvo, auxPos+pos)

    if(tamanho == 0):
        return(-1)






# pos = busca_sequencial(biglist, 22)
# print(str(pos))
# pos = busca_sequencial_sentinela(biglist, 25)
# print(str(pos))
# pos = busca_sequencial(biglist, 25)
# print(str(pos))
#
# index = cria_index(biglist, 10)
# pos = busca_sequencial_indexada(index, biglist, 998)
# print(str(pos))
# print('real: ' + str(biglist.index(998)))
# randnums = np.random.randint(1,999,200)
# randnums.sort()
# print(randnums)
# thisIndex = cria_index(randnums, 10)
# print(thisIndex)
pos = busca_binaria(list, 23, 0)
print(str(pos))
