from partida.Tabela import Tabela
from partida.Rodada import Rodada
from partida.Partida import Partida
from Time import Time





class Campeonato:
    def __init__(self, ano):
        self.__serieA = []
        self.__ano = ano
        self.__tabela = Tabela()
        self.__rodadas = []

    def addTime(self, timeNovo):
        if type(timeNovo) != Time:
            raise ValueError("O objeto deve ser do tipo time para ser adicionado ao campeonato!!")
        if(len(self.__serieA) < 6):
            self.__serieA.append(timeNovo)
        else:
            print("O campeonato deve ter apenas 6 times")

    def printTimes(self):
        for time in self.__serieA:
            print(time)

    def novaRodada(self):
        print("\n\n")
        r = ""
        while r != "V":
            r = input("Você deseja editar, criar uma nova rodada ou voltar?? (e,c ou v)").upper()
            if r == "E":
                if len(self.__rodadas) == 0:
                    print("Não Há rodada a ser editada!!")
                    continue
                else:
                    i = 1
                    time = 1
                    for rodada in self.__rodadas:
                        print(i)
                        i += 1
                    r1 = input('Qual rodada deseja editar?')
                    while r1.isdigit() == False:
                        r1 = input('Digite um numero inteiro valido:')
                    r1 = int(r1)
                    print(self.__rodadas[r1-1])
                    r2 = input('Qual partida deseja editar?')
                    while r2.isdigit() == False:
                        r2 = input('Digite um numero inteiro valido:')
                    r2= int(r2)
                    print(self.__rodadas[r1-1].jogos[r2-1])
                    partidaEdit = self.__rodadas[r1-1].jogos[r2-1]
                    for times in self.__serieA:
                        print(f"{time} {times}")
                        time += 1
                    escolhatimeA = ""
                    while escolhatimeA.isdigit() == False:
                        escolhatimeA = input(f"Digite o numero correspondente do time mandante da partida editada:)")
                    while int(escolhatimeA) > (len(self.__serieA)+1):
                        escolhatimeA = input("Escolha um time válido para o time Mandante:")
                    escolhatimeA = int(escolhatimeA)
                    escolhatimeB = ""
                    while (escolhatimeB.isdigit() == False):
                        escolhatimeB = input(f"Digite o numero correspondente do time visitante da partida editada")
                    while(int(escolhatimeB) == escolhatimeA) and (int(escolhatimeB > len(self.__serieA)+1)):
                        escolhatimeB = input("Escolha um time válido para o time visitante:")
                    escolhatimeB = int(escolhatimeB)
                    golsA = input(f"digite os gols do time mandante da partida editada")
                    while golsA.isdigit() == False:
                        golsA = input(f"Digite o numero correspondente de gols do time mandante da partida editada")
                    golsB = input(f"digite os gols do time visitante da partida editada")
                    while golsB.isdigit() == False:
                        golsB = input(f"Digite o numero correspondente de gols do do time visitante da partida editada")
                    timeA = self.__serieA[escolhatimeA-1]
                    timeB = self.__serieA[escolhatimeB - 1]
                    if partidaEdit.GolsA > partidaEdit.GolsB:
                        partidaEdit.Mandante.Pontos -= 3
                    elif partidaEdit.GolsA < partidaEdit.GolsB:
                        partidaEdit.Visitante.Pontos -= 3
                    elif partidaEdit.GolsA == partidaEdit.GolsB:
                        partidaEdit.Mandante.Pontos -= 1
                        partidaEdit.Visitante.Pontos -= 1
                    partidaEdit.Mandante = timeA
                    partidaEdit.Visitante = timeB
                    partidaEdit.GolsA = golsA
                    partidaEdit.GolsB = golsB
                    print(partidaEdit)
                    partidaEdit.pontos()
                    continue

            elif r == "C":
                novarodada = Rodada()
                partida = 1
                time = 1
                for partidas in range(3):
                    if partida == 1:
                        for times in self.__serieA:
                            print(f"{time} {times}")
                            time += 1
                    escolhatimeA = input(f"Digite o numero correspondente do time mandante da {partida}º partida ")
                    escolhatimeA = self.verificaNumeroValido(escolhatimeA)
                    escolhatimeA = int(escolhatimeA)

                    escolhatimeB = input(f"Digite o numero correspondente do time visitante da {partida}º partida ")
                    escolhatimeB = self.verificaNumeroValido(escolhatimeB)
                    escolhatimeB = int(escolhatimeB)
                    golsA = input(f"digite os gols do time mandante da {partida}º")
                    golsB = input(f"digite os gols do time visitante da {partida}º")
                    timeA = self.__serieA[escolhatimeA-1]
                    timeB = self.__serieA[escolhatimeB-1]
                    novapartida = Partida(timeA, timeB)
                    novapartida.GolsA = golsA
                    novapartida.GolsB = golsB
                    novarodada.jogos.append(novapartida)
                    partida += 1
                    novapartida.pontos()
                self.__rodadas.append(novarodada)
                continue



        return 0

    def verificaNumeroValido(self, escolha):
        if escolha.isdigit() == False:
            while escolha.isdigit() == False:
                escolha = input(f"Digite um numero Valido")
                if escolha.isdigit():
                    if int(escolha) < len(self.__serieA):
                        return escolha
        elif(escolha.isdigit() == True) and ((int(escolha) > (len(self.__serieA) + 1)) or int(escolha) == 0):
            while escolha.isdigit() == True:
                escolha = input(f"Digite um numero Valido")
                if (int(escolha) < (len(self.__serieA) + 1)) and int(escolha) != 0:
                    return escolha

        else:
            return escolha


    def checaFraudes(self):
        print("\n\n")
        #lista com todos os CPFs
        CPFs = []
        #lista com os CPFs repetidos
        CPFR = []
        #Pega todos os times do campeonato
        for times in self.__serieA:
            #pega todos os jogadores
            for Jogadores in times.Elenco:
                nome = Jogadores.Nome
                cpf = Jogadores.CPF
                #verifica se a lista 'CPFs' esta vazia
                if CPFs:
                    #coloca o cpf na lista 'CPFs'
                   CPFs.append([nome, cpf])
                    #pega todos os CPFs da lista e verifica se há algum repetido
                   for Nome, Cpf in CPFs:
                       if nome != Nome and cpf == Cpf:
                           r1 = [nome, cpf]
                           #Verifica se o cpf já não está na lista de CPF repetido
                           if r1 not in CPFR:
                               CPFR.append(r1)
                           r2 = [Nome, Cpf]
                           # Verifica se o cpf já não está na lista de CPF repetido
                           if r2 not in CPFR:
                               CPFR.append(r2)
                #se estiver vazia, coloca o primeiro CPF
                else:
                    CPFs.append([nome, cpf])



        print("Os seguintes jogadores possuem o CPF igual:")
        for nome, cpf in CPFR:
            print(f"Nome: {nome} CPF: {cpf}")



    def transferencia(self):
        print("\n\n")
        jogadores = []
        times = []
        # coloca os times do campeonato na lista 'times'
        for time in self.serieA:
            times.append(time)
            # coloca os jogadores do campeonato na lista'jogadores'
            for jogador in time.Elenco:
                jogadores.append(jogador)
        i = 1
        #mostra os jogadores com seus respectivos times
        for jogador in jogadores:
            print(f"{i} - {jogador.Nome} está no time {jogador.time}")
            i += 1
        Rjogador = ""
        # enquanto a variavel não for uma string com digito, pedira o numero do jogador
        while Rjogador.isdigit() != True:
            Rjogador = input("Qual o numero do jogador que será transferido??")
        # se o numero do jogador for maior que a lista pedira um numero valido
        while int(Rjogador) > len(jogadores):
            Rjogador = input(f"Digite um inteiro de 1 a {len(jogadores)}")
            while Rjogador.isdigit() != True:
                Rjogador = input("Digite um numero inteiro!!")
        Rjogador = int(Rjogador)
        # a variavel jogador guarda o jogador de acordo com o numero escolhido
        jogador = jogadores[Rjogador - 1]
        # time que envia é colocado numa variavel a partir do time atual do jogador
        timeEnvia = jogador.time
        i = 1
        for time in times:
            print(f"{i} - {time}")
            i += 1
        RtimeRecebe = ""
        # enquanto a variavel não for uma string com digito, pedira o numero do jogador
        while RtimeRecebe.isdigit() != True:
            RtimeRecebe = input("Qual o numero do time irá receber o jogador??")
        RtimeRecebe = int(RtimeRecebe)
        # se o numero do time for maior que a quantidade de times ou o time que recebe for igual ao time atual
        # criará um looping até ser um time valido
        while RtimeRecebe > len(times) or times[RtimeRecebe - 1] == timeEnvia:
            RtimeRecebe = input(f"O time deve ser de 1 a {len(times)} e não deve ser igual ao time atual do jogador: ")
            while RtimeRecebe.isdigit() != True:
                RtimeRecebe = input("Digite um numero inteiro?? ")
            RtimeRecebe = int(RtimeRecebe)
            while times[RtimeRecebe - 1] == timeEnvia:
                RtimeRecebe = input("O time a receber deve ser diferente do time atual do jogador: ")
                while RtimeRecebe.isdigit() != True:
                    RtimeRecebe = input("Digite um numero inteiro?? ")
                RtimeRecebe = int(RtimeRecebe)

        RtimeRecebe = int(RtimeRecebe)
        # o time que receberá o jogador é posto em uma variavel
        timeRecebe = times[RtimeRecebe - 1]
        # é feita a transferencia
        timeEnvia.Elenco.remove(jogador)
        timeRecebe.Elenco.append(jogador)
        jogador.time = timeRecebe
        print(f"O Jogador {jogador.Nome} foi transferido para o time {timeRecebe}")

    def listaCidades(self):
        print("\n\n")
        print("Cidades presentes no campeonato:")
        cidades = []
        for Time in self.__serieA:
            if Time.Cidade not in cidades:
                cidades.append(Time.Cidade)
            else:
                continue

        for cidade in cidades:
            print(cidade)


    def classificacao(self):
        print("\n\n")
        print("Classificação atual:")
        for time in self.__serieA:
            nome = time
            pontos = time.Pontos
            print(f"{nome}: {pontos} pontos")

    @property
    def serieA(self):
        return self.__serieA

    @serieA.setter
    def serieA(self, time):
        resp = input("Deseja remover ou adicionar um time??(r ou a)")
        resp = resp.upper()
        if(resp == "R"):
            self.__serieA.remove(time)
        elif(resp == "A"):
            self.__serieA.append(time)
        else:
            print("Resposta invalida")

    @property
    def ano(self):
        return (self.__ano)

    @ano.setter
    def ano(self, ano):
        self.__ano = ano


    @property
    def tabela(self):
        return self.__tabela

    @property
    def rodadas(self):
        return self.__rodadas

    @rodadas.setter
    def rodadas(self, rodada):
        resp = input("Deseja remover ou adicionar uma rodada??(r ou a)")
        resp = resp.upper()
        if (resp == "R"):
            self.__rodadas.remove(rodada)
        elif (resp == "A"):
            self.__rodadas.append(rodada)
        else:
            print("Resposta invalida")



