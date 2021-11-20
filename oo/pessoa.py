class Pessoa:
    def __init__(self, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f" Olá {id(self)}"

if __name__ == '__main__':
    ataide = Pessoa(nome = "Ataíde")
    luciano = Pessoa(ataide, nome = "Luciano")
    p = Pessoa("luciano")
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = "Ataíde"
    print(p.nome)