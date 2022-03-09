from partida.Partida import Partida

class Rodada:
    def __init__(self):
        self.__jogos = []

    def __str__(self):
        i = 1
        jogos = []
        for partida in self.__jogos:
            partidaSTR = f"{partida.__str__()}"
            jogos.append([f"{i}º", partidaSTR])
            i += 1

        return f"{jogos}"

    @property
    def jogos(self):
        return self.__jogos

    @jogos.setter
    def jogos(self, partida):
        self.__jogos = partida