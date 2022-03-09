from Jogador import Jogador


class Time:
    def __init__(self, nome, cidade):
        self.__Nome = nome
        self.__Cidade = cidade
        self.__Elenco = []
        self.__Pontos = 0

    def contrataJogador(self, jogador: Jogador, salario: float):
        self.__Elenco.append(jogador)
        jogador.salario = salario
        jogador.time = self

    def __str__(self):
        return self.__Nome

    @property
    def Nome(self):
        return self.__Nome

    @property
    def Cidade(self):
        return self.__Cidade

    @property
    def Elenco(self):
        return self.__Elenco
    @property
    def Pontos(self):
        return self.__Pontos

    @Pontos.setter
    def Pontos(self, quant):
        self.__Pontos = quant

    @Nome.setter
    def Nome(self, nome):
        self.__Nome = nome

    @Cidade.setter
    def Cidade(self, nome):
        self.__Cidade = nome

    @Elenco.setter
    def Elenco(self, nome):
        self.__Elenco.append(nome)