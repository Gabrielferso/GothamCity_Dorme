import os
from fluxo.cadastro import realizar_cadastro
from interfaces.inputs import ler_escolha_valida

class JogoCidadeDorme:
    def __init__(self):
        self.dicionario_jogadores = {} 
        self.jogadores_actifs = set()   
        self.lista_nomes = []           
        self.nome_batman_real = ""
        self.nome_coringa_real = ""
        self.nome_pinguim_real = ""
        self.vitimas_da_noite = set()   
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
        print(" 🐺 REVELAÇÃO DE PAPÉIS (ESTILO WEREWOLF) 🐺 ")
        print("="*50)
        opcao = input("Desejam descobrir as vossas funções no ecrã agora? (s/n): ").strip().lower()
        
        if opcao == 's':
            for nome in self.lista_nomes:
                self.limpar_tela()
                print(f"📢 Vez de [{nome}] aproximar-se do ecrã!")
                input("Pressione [ENTER] quando estiver SOZINHO para ver o seu papel...")
                
                personagem = self.dicionario_jogadores[nome]
                print(f"\n▶️ O teu papel secreto é: {personagem.papel} ◀️")
                
                input("\nPressione [ENTER] para APAGAR o ecrã...")
            self.limpar_tela()
            print("✅ Todos sabem os seus papéis! O jogo vai começar...")
        else:
            print("\n⏩ Pulando revelação.")
        input("\nPressione ENTER para iniciar a primeira noite...")

    def fase_da_noite(self):
        self.limpar_tela()
        print("\n🌙 A CIDADE DORME... Todos na mesa fecham os olhos.")
        print("-" * 50)
        
        self.vitimas_da_noite.clear()

        if self.nome_coringa_real in self.jogadores_ativos:
            input("\n[VILÃO] Quem for o CORINGA, abra os olhos e pressione [ENTER]...")
            self.limpar_tela()
            self.dicionario_jogadores[self.nome_coringa_real].realizar_acao_noturna(self)
            input("\nPressione [ENTER] e feche os olhos...")
            self.limpar_tela()
        
        if self.nome_pinguim_real and self.nome_pinguim_real in self.jogadores_ativos:
            input("\n[VILÃO] Quem for o PINGUIM, abra os olhos e pressione [ENTER]...")
            self.limpar_tela()
            self.dicionario_jogadores[self.nome_pinguim_real].realizar_acao_noturna(self)
            input("\nPressione [ENTER] e feche os olhos...")
            self.limpar_tela()
        
        if self.nome_batman_real in self.jogadores_ativos:
            input("\n[INVESTIGADOR] Quem for o BATMAN, abra os olhos e pressione [ENTER]...")
            self.limpar_tela()
            self.dicionario_jogadores[self.nome_batman_real].realizar_acao_noturna(self)
            input("\nPressione [ENTER] e feche os olhos...")
            self.limpar_tela()

        for vitima in list(self.vitimas_da_noite):
            if vitima in self.jogadores_ativos:
                self.jogadores_ativos.remove(vitima)
                self.dicionario_jogadores[vitima].status = "Eliminado"

    def fase_da_discussao_e_votacao(self):
        self.limpar_tela()
        print("\n☀️ A CIDADE ACORDA!")
        print("="*50)
        
        if self.vitimas_da_noite:
            print(f"💀 NOTÍCIA DE ÚLTIMA HORA: {', '.join(self.vitimas_da_noite)} foram eliminados esta noite!")
        else:
            print("🕊️ Milagre em Gotham! Ninguém foi eliminado esta noite.")
            
        print("="*50)
        print(f"👥 Sobreviventes na mesa: {', '.join(self.jogadores_ativos)}")
        print("="*50)
        
        ativos_lista = list(self.jogadores_ativos)
        print("  [0] Pular votação / Não prender ninguém no Arkham")
        for idx, nome in enumerate(ativos_lista, 1):
            print(f"  [{idx}] {nome}")
            
        voto = ler_escolha_valida("\nDigite o número de quem a mesa decidiu MANDAR para o Arkham: ", len(ativos_lista))
        
        if voto == 0:
            print("\nVotação inconclusiva! A cidade decidiu não prender ninguém hoje.")
        else:
            suspeito = ativos_lista[voto - 1]
            self.dicionario_jogadores[suspeito].status = "Preso no Arkham"
            self.jogadores_actifs.remove(suspeito)
            print(f"\n🔒 {suspeito} foi enviado para o Asilo Arkham!")
            
            if suspeito == self.nome_coringa_real and self.qtd_viloes_configurada == 2:
                self.coringa_ganhou_por_ejecao = True
                print(f"🃏 O Coringa ({self.nome_coringa_real}) começa a rir descontroladamente!")
                print("Ele queria ser pego para ativar o seu plano mestre!")
            elif suspeito in [self.nome_coringa_real, self.nome_pinguim_real]:
                print(f"🎉 Parabéns! Vocês prenderam um dos vilões infiltrados!")
            else:
                print(f"🤦‍♂️ Que erro! {suspeito} era apenas um Policial inocente!")
                
        input("\nPressione ENTER para continuar...")

    def verificar_vencedor(self):
        if self.coringa_ganhou_por_ejecao:
            print(f"\n🃏 VITÓRIA SOLO DO CORINGA ({self.nome_coringa_real})!")
            return True

        viloes_vivos = []
        if self.nome_coringa_real in self.jogadores_ativos:
            viloes_vivos.append(self.nome_coringa_real)
        if self.nome_pinguim_real and self.nome_pinguim_real in self.jogadores_ativos:
            viloes_vivos.append(self.nome_pinguim_real)

        if not viloes_vivos:
            print("\n🏆 VITÓRIA DOS INOCENTES! Todos os vilões foram desmascarados e presos!")
            return True
            
        if len(self.jogadores_ativos) <= len(viloes_vivos) + 1:
            print(f"\n🤡 VITÓRIA DOS VILÕES ({', '.join(viloes_vivos)})! O caos dominou Gotham City!")
            return True
        return False

    def jogar(self):
        realizar_cadastro(self)
        self.fase_revelacao_papeis()
        
        while True:
            self.fase_da_noite()
            if self.verificar_vencedor():
                break
            self.fase_da_discussao_e_votacao()
            if self.verificar_vencedor():
                break