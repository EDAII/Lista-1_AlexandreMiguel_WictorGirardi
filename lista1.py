import os
import numpy as np


def menu_principal():
    print("***************************************")
    print("**            MENU - LISTA 1         **")
    print("***************************************")
    print("**   1 - Gerar vetor aleatório       **")
    print("**   2 -                             **")
    print("**   3 -                             **")
    print("**   4 - Creditos                    **")
    print("**   0 - Sair                        **")
    print("***************************************")
    escolha = input("Digite uma Escolha: ")
    return escolha

def escolha_tamanho():
    print("Escolha o tamanho do vetor e o programa irá gerar-lo automaticamente!")
    tamanho = input("Digite o tamanho: ")
    tam = int(tamanho)
    randnums= np.random.randint(1,101,tam)
    return randnums

escolha = 0
while escolha != '100':
    escolha = menu_principal()
    if escolha == '1':
        print("O vetor aleatório é: \n")
        print(escolha_tamanho())
    elif escolha == '2':
        print("MEU FILHO\n")
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
