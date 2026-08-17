def contadorVogais(string):
    contador = 0
    for letra in string:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            contador += 1
    print(f'Há {contador} vogais na palavra {string}.')

palavra = input("Escreva uma palavra: ")
contadorVogais(palavra)