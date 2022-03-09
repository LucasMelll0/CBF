from Jogador import Jogador
from Time import Time
from Campeonato import Campeonato


class Principal:
    def __init__(self):
        self.primeiraExecucao()


    def primeiraExecucao(self):
        America = Time("America-MG", "Belo Horizonte")
        AtleticoMG = Time("Atlético-MG", "Belo Horizonte")
        AtleticoPR = Time("Atlético-PR", "Curitiba")
        AtleticoGO = Time("Atlético-Go", "Goiânia")
        Bahia = Time("Bahia", "Bahia")
        Bragantino = Time("Red Bull Bragantino", "Bragança Paulista")

        Joao = Jogador("João", "115544", "444666777", "01/01/2000", "RJ", "Sem time", 0.0)
        Pedro = Jogador("Pedro", "115544", "222444555", "21/11/2001", "RJ", "Sem time", 0.0)
        Victor = Jogador("Victor", "555544", "444999888", "04/03/1999", "SP", "Sem time", 0.0)
        Pablo = Jogador("Pablo", "125544", "999888111", "08/05/1998", "MG", "Sem time", 0.0)
        Neymar = Jogador("Neymar", "115544", "888999444", "15/10/2005", "CE", "Sem time", 2.0)
        Messi = Jogador("Messi", "515544", "222777666", "28/02/2004", "TO", "Sem time", 0.0)

        br2021 = Campeonato(2021)
        self.campeonatoatual = br2021

        br2021.addTime(America)
        br2021.addTime(AtleticoMG)
        br2021.addTime(AtleticoPR)
        br2021.addTime(AtleticoGO)
        br2021.addTime(Bahia)
        br2021.addTime(Bragantino)

        America.contrataJogador(Joao, 1400)
        AtleticoMG.contrataJogador(Pedro, 18000)
        AtleticoPR.contrataJogador(Victor, 3500)
        AtleticoGO.contrataJogador(Pablo, 38000)
        Bahia.contrataJogador(Neymar, 9999999)
        Bragantino.contrataJogador(Messi, 10)

        print("Este é o programa para controle do campeonato brasileiro")

        while (len(br2021.rodadas)) < 12:
            print(f"\n\nAtualmente estamos na rodada {len(br2021.rodadas)+1}, Oque deseja fazer?")
            print("1 - Registrar nova rodada")
            print("2 - Registrar Registrar transferencia de jogador")
            print("3 - Checar fraudes em CPF")
            print("4 - Listar cidades dos times")
            print("5 - Checar classificação atual")
            opcao = input("Escolha: ")
            while opcao.isdigit() == False:
                opcao = input("Coloque um numero inteiro de 1 a 5")
            opcao = int(opcao)

            if opcao == 1:
                if br2021.novaRodada() == 0:
                    continue
            elif opcao == 2:
                br2021.transferencia()
            elif opcao == 3:
                br2021.checaFraudes()
            elif opcao == 4:
                br2021.listaCidades()
            elif opcao == 5:
                br2021.classificacao()
            else:
                print(f"opção {opcao} não existe!!")




prin = Principal()
