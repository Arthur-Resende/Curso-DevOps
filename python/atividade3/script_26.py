frase = input("Frase: ")
primeiro_a = frase.find('a')

# encontra index do primeiro a na frase invertida
# adiciona 1 pois index invertido começa por -1, já index normal por 0
# subtrai pelo tramanho total da frase

ultimo_a = len(frase) - (frase[::-1].find('a') + 1)

print("A aparece %d vezes" %frase.count('a'))
print("Primeira aparicão: %d" %primeiro_a)
print("Primeira aparicão: %d" %ultimo_a)