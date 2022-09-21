from importlib.resources import Package
from xmlrpc.server import DocCGIXMLRPCRequestHandler
from mundo_das_ideias.class_dog import Dog

class Poodle(Dog):
    def __init__(self, nome, idade, tamanho):
        super().__init__(nome, idade)
        self.tamanho = tamanho

def escrever_cachorro(dog):
    print(dog.nome,"tem",dog.idade,"anos e",dog.tamanho,"metros")

dudu = Poodle('dudu', 4, 20)
escrever_cachorro(dudu)
dudu.puddle_rolar()