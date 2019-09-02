import os
import numpy as np
import time

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
    for numb in range(tamanho):
        if(lista[numb] == alvo):
            return numb
    else:
        return(-1)

# Esse método altera a lista que é passada como parâmetro
def busca_sequencial_sentinela(lista, alvo):
    np.append(alvo, lista)
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
    if(lista[sup] == lista[inf]):
        if(lista[inf] == alvo):
            return inf
        else:
            return -1

    meio = inf + int( (sup - inf) * ( (alvo - lista[inf]) / (lista[sup] - lista[inf]) ) )
    if( (lista[inf] > alvo) or (lista[sup] < alvo)):
        return -1
    elif(lista[meio] < alvo):
        return busca_interpolacao(lista, alvo, meio+1, sup)
    elif(lista[meio] > alvo):
        return busca_interpolacao(lista, alvo, inf, meio-1)
    else:
        return meio

# Funcoes uteis

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

# Funcao para menu principal
def menu_principal():
    print("*******************************************")
    print("**            MENU - LISTA 1             **")
    print("*******************************************")
    print("**   1 - Iniciar uma nova partida        **")
    print("**   2 - Executar buscas fora de um jogo **")
    print("**   3 - Créditos                        **")
    print("**   0 - Sair                            **")
    print("*******************************************")
    escolha = input("Digite uma Escolha: ")
    return escolha

# Funcao para escolha de tamanho de vetor e criacao do mesmo
def escolha_tamanho():
    print("Primeiramento,escolha o tamanho do vetor")
    tamanho = input("Digite o tamanho: ")
    tam = int(tamanho)
    randnums= np.random.randint(1,101,tam)
    randnums.sort()
    return randnums

# Funcao para escolha do metodo de busca desejado
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

# Funcao para escolha do elemento que deseja ser buscado
def escolha_elemento():
    print("Escolha o elemento que voce deseja buscar\n")
    escolhaElemento = input("Digite sua Escolha: ")
    escolha = int(escolhaElemento)
    return escolha

# Inicializacao de variaveis para execucao
escolhaBusca = 0
escolha = 0
escolhaJogo = 0
ponto = 0

# Loop do menu do programa
while escolha != '100':
    escolha = menu_principal()
    # escolha 1 - Jogo
    if escolha == '1':
        print("Bem vindo ao nosso jogo! Aqui iremos comparar a velocidade dos nossos métodos de busca\n")
        print("Vamos ver se voce é capaz de acertar!\n")
        print("Q1 - Possuindo um vetor de tamanho igual a 20, qual algoritmo será mais rapido em uma busca?\n")
        print("1 - busca Binaria")
        print("2 - busca Sequencial")
        escolhaJogo = input("Digite sua Escolha: ")
        if escolhaJogo == '1':
            ponto += 1
        else:
            ponto += 0
        print("Q2 - Possuindo um vetor de tamanho igual a 50, qual algoritmo será mais rapido em uma busca?\n")
        print("1 - busca Sequencial indexada")
        print("2 - busca Sequencial")
        escolhaJogo = input("Digite sua Escolha: ")
        if escolhaJogo == '2':
            ponto += 1
        else:
            ponto += 0
        print("Q3 - Agora com um vetor de tamanho igual a 100, qual algoritmo será mais rapido em uma busca?\n")
        print("1 - busca sequencial com sentinela")
        print("2 - busca Binaria")
        escolhaJogo = input("Digite sua Escolha: ")
        if escolhaJogo == '1':
            ponto += 1
        else:
            ponto += 0
        print("Q4 - Com um vetor de tamanho igual a 10, qual algoritmo será mais rapido em uma busca?\n")
        print("1 - Busca sequencial indexada")
        print("2 - busca sequencial")
        escolhaJogo = input("Digite sua Escolha: ")
        if escolhaJogo == '2':
            ponto += 1
        else:
            ponto += 0
        print("Q5 - Qual desses algoritmos necessitam estar ordenados para funcionar?\n")
        print("1 - Busca sequencial indexada")
        print("2 - busca sequencial com Sentinela")
        escolhaJogo = input("Digite sua Escolha: ")
        if escolhaJogo == '1':
            ponto += 1
        else:
            ponto += 0
        if ponto > 3:
            print("Parabens! Voce acertou %s pontos!" % (ponto))
            ponto = 0
        else:
            print("Voce poderia ter se saido melhor! Voce acertou %s pontos" % (ponto))
            ponto = 0
        # Escolha 2 - Buscas fora do jogo
    elif escolha == '2':
                escolhaTamanho = escolha_tamanho()
                print(escolhaTamanho)
                escolhaBusca = escolha_busca()
                if escolhaBusca == '1':
                    escolhaElemento = escolha_elemento()
                    print(escolhaElemento)
                    start_time = time.time()
                    buscaBinaria = busca_binaria(escolhaTamanho, escolhaElemento, 0)
                    if buscaBinaria == -1:
                        print("O elemento nao foi encontrado")
                        print("A busca levou %s segundos para ser executada" % (time.time() - start_time))
                    else:
                        print("A busca levou %s segundos para ser executada" % (time.time() - start_time))
                        print("O elemento esta na posicao: %s" % buscaBinaria)
                elif escolhaBusca == '2':
                    escolhaElemento = escolha_elemento()
                    tamanho = len(escolhaTamanho)
                    start_time = time.time()
                    busca = busca_interpolacao(escolhaTamanho, escolhaElemento, 0 , tamanho - 1 )
                    if busca == -1:
                        print("O elemento nao foi encontrado")
                        print("A busca levou %s segundos para ser executada" % (time.time() - start_time))
                    else:
                        print("A busca levou %s segundos para ser executada" % (time.time() - start_time))
                        print("O elemento esta na posicao: %s" % busca)
                elif escolhaBusca == '3':
                    escolhaElemento = escolha_elemento()
                    print(escolhaElemento)
                    start_time = time.time()
                    buscaSequencial= busca_sequencial(escolhaTamanho, escolhaElemento)
                    if buscaSequencial == -1:
                        print("O elemento nao foi encontrado")
                        print("A busca levou %s segundos para ser executada" % (time.time() - start_time))
                    else:
                        print("A busca levou %s segundos para ser executada" % (time.time() - start_time))
                        print("O elemento esta na posicao: %s" % buscaSequencial)
                elif escolhaBusca == '4':
                    escolhaElemento = escolha_elemento()
                    print(escolhaElemento)
                    index_index =  int(len(escolhaTamanho)/2)
                    index = cria_index(escolhaTamanho, index_index)
                    start_time = time.time()
                    buscaSequencialIndexada = busca_sequencial_indexada(index, escolhaTamanho, escolhaElemento)
                    if buscaSequencialIndexada == -1:
                        print("O elemento nao foi encontrado")
                        print("A busca levou %s segundos para ser executada" % (time.time() - start_time))
                    else:
                        print("A busca levou %s segundos para ser executada" % (time.time() - start_time))
                        print("O elemento esta na posicao: %s" % buscaSequencialIndexada)
                elif escolhaBusca == '5':
                    escolhaElemento = escolha_elemento()
                    print(escolhaElemento)
                    start_time = time.time()
                    buscaSequencialSentinela = busca_sequencial_sentinela(escolhaTamanho, escolhaElemento)
                    if buscaSequencialSentinela == -1:
                        print("O elemento nao foi encontrado")
                        print("A busca levou %s segundos para ser executada" % (time.time() - start_time))
                    else:
                        print("A busca levou %s segundos para ser executada" % (time.time() - start_time))
                        print("O elemento esta na posicao: %s" % buscaSequencialSentinela)
                else:
                    print('Opção Invalida! Tente novamente')
        # Créditos
    elif escolha == '3':
        print("\n**************************************")
        print("Esse trabalho foi feito com carinho pelos alunos:")
        print("Alexandre Miguel Rodrigues Nunes Pereira - Matricula: 16/0000840")
        print("Wictor Bastos Girardi - Matricula: 17/0047326")
        print("**************************************\n\n")
        # Sair do programa
    elif escolha == '0':
        print("Obrigado por usar, volte sempre!\n")
        break
        # Caso o usuario tenha entrado com um valor invalido
    else:
        print('Opção Invalida! Tente novamente')
