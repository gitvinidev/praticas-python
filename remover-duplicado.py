def removerDuplicado(lista):
    listaDois = []
    lista.sort()
    for x in lista:
        if x not in listaDois:
            listaDois.append(x)
    return listaDois
            

numeros = [2, 4, 5, 6, 4, 2, 3, 3, 7, 9, 9]
print(removerDuplicado(numeros))