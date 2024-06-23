def verifica_pari_dispari(numero):
    if numero % 2 == 0:
        return f"Il numero {numero} è pari."
    else:
        return f"Il numero {numero} è dispari."

numero = 7
output = verifica_pari_dispari(numero)
print(output)
