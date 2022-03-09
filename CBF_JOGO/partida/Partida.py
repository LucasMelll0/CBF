from Time import Time
class Partida:
    def __init__(self, casa: Time, visitante: Time):
        self.__Mandante = casa
        self.__Visitante = visitante
        self.__TitularA = casa.Elenco
        self.__TitularB = visitante.Elenco
        self.__GolsA = 0
        self.__GolsB = 0

    def getCidadeJogo(self):
        print(self.__Mandante.Cidade)

    def getResultado(self):
        if(self.__GolsA < self.__GolsB):
            return -1
        elif(self.__GolsA == self.GolsB):
            return 0
        else:
            return 1

    def ResultadoRegistrado(self):
        print(f"{self.__Mandante}: {self.__GolsA} X {self.__Visitante}: {self.__GolsB}")

    def pontos(self):
        if self.__GolsA > self.__GolsB:
            self.__Mandante.Pontos += 3
        elif(self.__GolsA < self.__GolsB):
            self.__Visitante.Pontos += 3
        elif(self.__GolsA == self.__GolsB):
            self.__Mandante.Pontos += 1
            self.__Visitante.Pontos += 1


    def __str__(self):
        return f"timeA: {self.__Mandante} {self.__GolsA} X  timeB: {self.__Visitante} {self.__GolsB}"


    @property
    def Mandante(self):
        return self.__Mandante

    @property
    def Visitante(self):
        return self.__Visitante

    @property
    def GolsA(self):
        return self.__GolsA

    @property
    def GolsB(self):
        return self.__GolsB

    @Mandante.setter
    def Mandante(self, casa):
        if type(casa) == Time:
            self.__Mandante = casa
        else:
            print("Mandante precisa ser da classe Time!!")


    @Visitante.setter
    def Visitante(self, visita):
        if type(visita) == Time:
            self.__Visitante = visita
        else:
            print("Visitante precisa ser da classe Time!!")

    @GolsA.setter
    def GolsA(self, quant):
        if quant.isdigit():
            quant = int(quant)
            self.__GolsA = quant
        # se a string estiver vazia reconhece como nenhum gol
        elif (not quant) or (quant.isdigit) == False:
            self.__GolsA = 0

    @GolsB.setter
    def GolsB(self, quant):
        if quant.isdigit():
            quant = int(quant)
            self.__GolsB = quant
        # se a string estiver vazia reconhece como nenhum gol
        elif(not quant) or (quant.isdigit) == False:
            self.__GolsB = 0