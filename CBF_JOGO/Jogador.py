from Pessoa import Pessoa


class Jogador(Pessoa):

    def __init__(self, nome, CPF, RG, Nascimento, estado, Time_Atual, Salario: float):
        super().__init__(nome, CPF, RG, Nascimento, estado)
        self.__time = Time_Atual
        self.__salario = float(Salario)

    @property
    def time(self):
        return self.__time

    @property
    def salario(self):
        return self.__salario

    @time.setter
    def time(self, time):
        self.__time = time

    @salario.setter
    def salario(self, salario):
        self.__salario = salario
