import os
from jogo.cadastro import executar_cadastro
from jogo.noite import executar_fase_noite
from jogo.votacao import executar_fase_votacao

class JogoCidadeDorme:
    def __init__(self):
        self.dicionario_jogadores = {} 
        self.jogadores_actifs = set()   
        self.lista_nomes = []           
        self.nome_batman_real = ""
        self.nome_coringa_real = ""
        self.nome_pinguim_real = ""
        self.vitimas_da_noite = set()   
        self.jogador_silenciado = ""
        self.coringa_ganhou_por_ejecao = False 
        self.qtd_viloes_configurada = 1  

    @property
    def jogadores_ativos(self):
        return self.jogadores_actifs

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def fase_revelacao_papeis(self):
        self.limpar_tela()
        print("="*50)
        print(" 🦇 REVELAÇÃO DE PAPÉIS 🤡 ")
        print("="*50)
        print("Pressione [ENTER] para revelar os papéis...")
        
        for nome in self.lista_nomes:
            self.limpar_tela()
            print(f"📢 Vez de [{nome}] aproximar-se da tela!")
            input("Pressione [ENTER] quando estiver SOZINHO para ver o seu papel...")
                
            personagem = self.dicionario_jogadores[nome]
            print(f"\n▶️ O teu papel secreto é: {personagem.papel} ◀️")
                
            input("\nPressione [ENTER] para APAGAR sua função...")
        self.limpar_tela()
        print("✅ Todos sabem os seus papéis! O jogo vai começar...")

    def verificar_vencedor(self):
        if self.qtd_viloes_configurada == 2:
            if self.coringa_ganhou_por_ejecao:
                print(f"\n🃏 VITÓRIA SOLO DO CORINGA ({self.nome_coringa_real})!")
                return True
            else:
                viloes_vivos = []
                if self.nome_coringa_real in self.jogadores_ativos:
                    viloes_vivos.append(self.nome_coringa_real)
                if self.nome_pinguim_real in self.jogadores_ativos:
                    viloes_vivos.append(self.nome_pinguim_real)

                if not viloes_vivos:
                    print("\n🏆 VITÓRIA DOS INOCENTES! Todos os vilões foram desmascarados e presos!")
                    return True
                    
                if len(self.jogadores_ativos) <= len(viloes_vivos) + 1:
                    print(f"\n🤡 VITÓRIA DOS VILÕES ({', '.join(viloes_vivos)})! O caos dominou Gotham City!")
                    return True

    def jogar(self):
        executar_cadastro(self)
        self.fase_revelacao_papeis()
        
        while True:
            executar_fase_noite(self)
            if self.verificar_vencedor():
                break
            executar_fase_votacao(self)
            if self.verificar_vencedor():
                break