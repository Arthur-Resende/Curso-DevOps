frase = input("Frase: ").lower()
primeiro_a = frase.find('a')
ultimo_a = len(frase) - (frase[::-1].find('a') + 1)

print("A aparece %d vezes" %frase.count('a'))
print("Primeira aparicão: %d" %primeiro_a)
print("Última aparicão: %d" %ultimo_a)

# print("string {}".format(something))