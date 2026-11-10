class Pessoa:
    def __init__(self, nome, idade, **kwargs):
        self.nome = nome
        self.idade = idade

        print(kwargs)
        
class Programador(Pessoa):
    def __init__ (self, nome, idade, linguagem, **kwargs):
        super().__init__(nome, idade, **kwargs)
        self.linguagem = linguagem



programador = Programador(
    "Silvo",
    30,
    linguagem="Python",
    salario = 5000,
    exeperiencia = "5 anos"
)

print(programador.nome)
print(programador.idade)
print(programador.linguagem)