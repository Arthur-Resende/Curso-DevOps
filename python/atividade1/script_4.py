valor = input("Escreva um valor (numerico ou não) qualquer: ")
# verificando caracteristicas
numerico = valor.isnumeric()

alfabetico = False
for char in valor:
    if char.isnumeric():
        alfabetico = False
        break
    else:
        alfabetico = True

alfanumerico = not (numerico or alfabetico)
maiuscula = valor.isupper()
minuscula = valor.islower()
capitalizada = True if valor[0].isupper() else False

# Escrevendo características e tipo
if alfanumerico:
    tipo_char = "alfanumerico"
    print(type(valor))
elif numerico:
    tipo_char = "numerico"
    print(type(int(valor)))
else:
    tipo_char = "alfabetico"
    print(type(valor)) 

# Escrevendo capitalização
if capitalizada:
    caixa = "e capitalizado"
elif minuscula:
    caixa = "e escrito em caixa baixa"
elif maiuscula:
    caixa = "e escrito em caixa alta"
else:
    caixa = ""
print("valor é %s %s" %(tipo_char,caixa))
