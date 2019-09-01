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

# Busca binária com criação de novo vetor a cada iteração
def busca_binaria(lista, alvo, auxPos):
    print(lista)
    tamanho = len(lista)
    pos = (tamanho//2)
    novaLista = []
    if(lista[pos] == alvo):
        return pos + auxPos
    elif(tamanho == 1):
        return(-1)
    elif(lista[pos] > alvo):
        for elemento in range(pos):
            novaLista.append(lista[elemento])
        return busca_binaria(novaLista, alvo, auxPos)
    elif(lista[pos] < alvo):
        for elemento in range(pos, tamanho, 1):
            novaLista.append(lista[elemento])
        return busca_binaria(novaLista, alvo, auxPos+pos)


# Busca por interpolação
def busca_interpolacao(lista, alvo, inf, sup):
    #Caso tenha apenas um elemento na lista
    # print("\n[", end="")
    # for numb in range(inf, sup+1, 1):
    #     print(str(lista[numb]), end=", ")
    # print("]", end="")
    print('inf: ' + str(inf) + ' ' + 'sup: ' + str(sup))
    if(lista[sup] == lista[inf]):
        if(lista[inf] == alvo):
            return inf
        else:
            return -1

    meio = inf + int( (sup - inf) * ( (alvo - lista[inf]) / (lista[sup] - lista[inf]) ) )
    print('meio: ' + str(meio))
    print('heheh')
    if( (lista[inf] > alvo) or (lista[sup] < alvo)):
        return -1
    elif(lista[meio] < alvo):
        return busca_interpolacao(lista, alvo, meio+1, sup)
    elif(lista[meio] > alvo):
        return busca_interpolacao(lista, alvo, inf, meio-1)
    else:
        return meio






# pos = busca_sequencial(biglist, 22)
# print(str(pos))
# pos = busca_sequencial_sentinela(biglist, 25)
# print(str(pos))
# pos = busca_sequencial(biglist, 25)
# print(str(pos))
# index = cria_index(biglist, 10)
# pos = busca_sequencial_indexada(index, biglist, 998)
# print(str(pos))
# print('real: ' + str(biglist.index(998)))
# randnums = np.random.randint(1,999,200)
# randnums.sort()
# print(randnums)
# thisIndex = cria_index(randnums, 10)
# print(thisIndex)
# pos = busca_binaria(list, 1, 0)
# print(str(pos))
# print('real: ' + str(biglist.index(762)))
# pos = busca_interpolacao(biglist, 15, 0, 199)
# print(str(pos))

def menu_principal():
    print("*******************************************")
    print("**            MENU - LISTA 1             **")
    print("*******************************************")
    print("**   1 - Iniciar uma nova partida        **")
    print("**   2 - Executar buscas fora de um jogo **")
    print("**   3 -                                 **")
    print("**   4 - Créditos                        **")
    print("**   0 - Sair                            **")
    print("*******************************************")
    escolha = input("Digite uma Escolha: ")
    return escolha

def escolha_tamanho():
    print("Primeiramento,escolha o tamanho do vetor")
    tamanho = input("Digite o tamanho: ")
    tam = int(tamanho)
    randnums= np.random.randint(1,101,tam)
    return randnums

def escolha_busca():
    print("Agora escolha seu método de busca desejado\n")
    print("*******************************************")
    print("**   1 - Busca Binaria                   **")
    print("**   2 - Busca por interpolaçao          **")
    print("**   3 - Busca sequencial                **")
    print("**   4 - Busca sequencial indexada       **")
    print("**   5 - Busca sequencial com sentinela  **")
    print("*******************************************")
    escolhaBusca = input("Digite sua Escolha: ")
    return escolhaBusca

escolhaBusca = 0
escolha = 0

while escolha != '100':
    escolha = menu_principal()
    if escolha == '1':
        print("O vetor aleatório é: \n")
        print(escolha_tamanho())
        escolha_busca()
    elif escolha == '2':
        escolha_tamanho()
        print(randnums)
    elif escolha == '3':
        print("MEU ALE\n")
    elif escolha == '4':
        print("\n**************************************")
        print("Esse trabalho foi feito com carinho pelos alunos:")
        print("Alexandre Miguel Rodrigues Nunes Pereira - Matricula: 16/0000840")
        print("Wictor Bastos Girardi - Matricula: 17/0047326")
        print("**************************************\n\n")
    elif escolha == '0':
        print("Obrigado por usar, volte sempre!\n")
        break
    else:
        print('Opção Invalida! Tente novamente')

while escolhaBusca != '100':
    escolhaBusca = escolha_busca()
    if escolha == '1':
        print("O vetor aleatório é: \n")
        print(escolha_tamanho())
    elif escolha == '2':
        escolha_tamanho()
        print(randnums)
    elif escolha == '3':
        print("MEU ALE\n")
    elif escolha == '4':
        print("\n**************************************")
        print("Esse trabalho foi feito com carinho pelos alunos:")
        print("Alexandre Miguel Rodrigues Nunes Pereira - Matricula: 16/0000840")
        print("Wictor Bastos Girardi - Matricula: 17/0047326")
        print("**************************************\n\n")
    elif escolha == '5':
        print("Obrigado por usar, volte sempre!\n")
    else:
        print('Opção Invalida! Tente novamente')
