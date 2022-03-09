from abc import ABC
from datetime import datetime

class Pessoa(ABC):

    def __init__(self, nome, CPF, RG, nascimento, estado):
        self.__Nome = nome
        self.__CPF = CPF
        self.__RG = RG
        self.__Nascimento = datetime.strptime(nascimento, '%d/%m/%Y').date()
        self.__Estado = estado

    @property
    def Nome(self):
        return  self.__Nome

    @property
    def CPF(self):
        return self.__CPF

    @property
    def RG(self):
        return self.__RG

    @property
    def Nascimento(self):
        return self.__Nascimento

    @property
    def Estado(self):
        return self.__Estado


    @Nome.setter
    def Nome(self,nome):
        self.__Nome = nome

    @CPF.setter
    def CPF(self, CPF):
        self.__CPF = CPF

    @RG.setter
    def RG(self, RG):
        self.__RG = RG

    @Nascimento.setter
    def Nascimento(self, data):
        self.__Nascimento = datetime.strptime(data, '%d/%m/%Y').date()

    @Estado.setter
    def Estado(self, estado):
        self.__Estado = estado

    def verificaEstado(self):
        estado = ["AC", "AL", "AP", "AM", "BA", "CE", "DF",
                  "ES", "GO", "MA", "MT", "MS",
                  "MG", "PA", "PB", "PR",
                  "PE", "PI", "RJ", "RN", "RS",
                  "RO", "RR", "SC", "SP", "SE", "TO"
                  ]

        for estados in estado:
            if self.__Estado in estado:
                return True
            else:
                return False


    def calculaIdade(self):
        hoje = datetime.today().date()
        idade = abs((self.__Nascimento - hoje).days)
        idade = int(idade/365.5)
        return idade
