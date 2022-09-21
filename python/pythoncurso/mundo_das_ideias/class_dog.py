class Dog:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def modificador(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def rolar(self):
        print("%s acaba de rolar!" %self.nome)
    
    def sentar(self):
        print("%s está sentado" %self.nome)

