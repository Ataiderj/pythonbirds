



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
    >>> direcao.girar_a_direita()
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
    >>> carro.acelerar()
    >>> carro.calcular_velocidade
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade
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

class Motor:
    def __init__(self):
        self.velocidade = velocidade

    def acelerar(self):
        self.acelerar = acelerar

    def frear(self):
        self.frear = frear
    def direcao (self):
        self.direcao = direcao


