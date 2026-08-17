def maior(a, b, c):
    if a > b > c or a > c > b:
        return a
    elif b > a > c or b > c > a:
        return b
    else:
        return c

numero1 = int(input("Primeiro número:"))

numero2 = int(input("Segundo número:"))

numero3 = int(input("Terceiro número:"))

print(f"O maior número é {maior(numero1, numero2, numero3)}")