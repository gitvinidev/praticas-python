def retornarFrequencia(lista):
    lista.sort()
    lista2 = list(set(lista))
    return {x: lista.count(x) for x in lista}

lista = ['python', 'laranja', 'python', 'morango', 'laranja', 'banana']
print(retornarFrequencia(lista))
