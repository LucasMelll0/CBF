class Tabela:
    def __init__(self):
        self.__Classificacao = ''

    @property
    def Classificacao(self):
        return self.__Classificacao

    @Classificacao.setter
    def Classificacao(self, classi):
        self.__Classificacao = classi