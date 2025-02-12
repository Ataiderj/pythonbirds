"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:
1) Motor
2) Direção

O motor terá a responsabilidade de controlar a velocidade.
ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incrementar a velocidade de uma unidades
3) Método frear que deverá decrementar a velocidade em duas unidades

Adireção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método girar a direita


    N
O      L
    S

    Exemplo:

    >>> motor = Motor()

    >>>motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    >>> # Tested Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    "Norte"
    >>> assert isinstance(direcao, )
direcao.girar_a_direita()
    >>> direcao.valor
    "Oeste"
     >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    "Sul"
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    "leste"
     >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    "Norte"
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade
    0
    >>> assert isinstance(carro.acelerar, )
carro.acelerar()
    >>> carro.calcular_velocidade
    1
    >>> carro.acelerar()
  object  >>> carro.calcular_velocidade
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade
    0
    >>> carro.calcular_direcao()
    "Norte"
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    "Leste"
"""
NORTE = "Norte"
SUL = "Sul"
LESTE = "Leste"
OESTE = "Oeste"


class Direcao: rotacao_a_direita_dct={
    NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
}
    rotacao_a_esquerda_dct = {
        NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL
    }
    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]
    def gira_a_esuerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]


    def acelerar(self, acelerar=None):
        self.acelerar = acelerar

    def frear(self, frear=None):
        self.frear = frear

    def direcao(self, direcao=None):
        self.direcao = direcao

        def girar_a_esquerda(self, girar_a_esquerda=None):
        self.girar_a_esquerda = girar_a_esquerda

class Motor:
    def __init__(self):
        self.velocidade = 0
    def acelerar(self):
        self.velocidade += 1
    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)






