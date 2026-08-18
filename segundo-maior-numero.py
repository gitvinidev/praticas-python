def segundoMaiorNumero(lista):
    lista.remove((max(lista)))
    return max(lista)

lista = [3, 545, 324, 478, 333]
print(segundoMaiorNumero(lista))