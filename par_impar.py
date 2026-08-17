def par_ou_impar(n):
    if n%2==0:
        return "par"
    else:
        return "impar"

numero = int(input("Digite um número: "))

print(par_ou_impar(numero))
