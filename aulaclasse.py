class Futebol:
    def __init__(self, time, campeonato):
        self.time = time
        self.campeonato = campeonato
        
    def meutime(self):
        print(f"Eu torço para {self.time}")
        
        if self.time == 'Flamengo':
            print("Você é um campeão!!")
        else:
            print("Você é um sofredor.")
    
    def jogo(self):
        print(f'O {self.time} vai jogar o campeonato {self.campeonato}.')
    
        
class Jogador(Futebol):
    def __init__(self, time, campeonato, nome, posicao):
        super().__init__(time, campeonato)
        self.nome = nome
        self.posicao = posicao

    def nome_jogador(self):
        print(f'{self.nome} joga pelo {self.time}.')
    
    def jogador_posicao(self):
        print(f'{self.nome} é {self.posicao}.')
        


        
time1 = Futebol("Flamengo", "Mundial")
time2 = Futebol("Vasco", "Série C")
time3 = Futebol("Real Madrid", "La liga")
jogador1 = Jogador("Flamengo", "Mundial", "Ronaldinho", "Meio campista")
jogador2 = Jogador("Vasco", "Série C", "Presunto", "Atacante")
jogador3 = Jogador("Real Madrid", "La liga", "Cristiano Ronaldo", "Atacante")

jogador1.meutime()
jogador1.jogo()
jogador1.nome_jogador()
jogador1.jogador_posicao()     