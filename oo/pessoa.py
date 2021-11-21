
class Pessoa:
    olhos = 2
    def __init__(self, *filhos,nome=None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f" Olá {id(self)}"
    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f"{cls} = olhos {cls.olhos}"

if __name__ == '__main__':
    ataide = Pessoa(nome = "Ataíde")
    luciano = Pessoa(ataide, nome = "Luciano")
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = "Ramalho"
    print(luciano.sobrenome)
    del luciano.filhos
    print(luciano.__dict__)
    print(ataide.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(ataide.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(ataide))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico(), ataide.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(),luciano.metodo_estatico())


