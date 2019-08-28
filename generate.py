
list = [8, 41, 50, 34, 10, 2, 13, 23, 27, 49]

def busca_sequencial(lista):
    for element in lista:
        for other_element in lista:
            if (element == other_element):
                print('\033[1m' + str(other_element) + '\033[0m', end = " ")
            else:
                print(str(other_element), end = " ")
        print('\n')
    return


busca_sequencial(list)
