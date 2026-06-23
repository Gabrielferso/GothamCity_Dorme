import os
import random

# ==========================================
# 1. TRATAMENTO DE EXCEÇÃO PERSONALIZADA
# ==========================================
class PersonagemNoArkhamError(Exception):
    """Lançada se um participante preso tentar realizar ações ou ser investigado."""
    def __init__(self, nome):
        self.nome = nome
        super().__init__(f"🚨 {nome} está trancado no Asilo Arkham e não pode agir/ser alvo!")

# ==========================================
# 2. ARQUITETURA DE CLASSES (POO)
# ==========================================
class Personagem:
    def __init__(self, nome: str, papel: str):
        self.nome = nome
        self.papel = papel
        self.__status = "Ativo"  # Encapsulamento: Atributo privado

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, novo_status):
        if novo_status in ["Ativo", "Preso no Arkham", "Eliminado"]:
            self.__status = novo_status

    def realizar_acao_noturna(self, jogo_contexto):
        """Método base que será polimórfico nas subclasses."""
        pass


class Batman(Personagem):
    def __init__(self, nome: str):
        super().__init__(nome, papel="🕵️‍♂️ DETETIVE (BATMAN)")

    # POLIMORFISMO: O Batman investiga se alguém é o vilão
    def realizar_acao_noturna(self, jogo_contexto):
        print(f"\n🦇 [BAT-SINAL] Vez do Investigador Secreto agir...")
        
        suspeitos_vivos = [p for p in jogo_contexto.jogadores_ativos]
        
        for idx, nome in enumerate(suspeitos_vivos, 1):
            print(f"  [{idx}] {nome}")
            
        try:
            escolha = int(input("\n(Investigador, digite o número do suspeito em segredo): ")) - 1
            if 0 <= escolha < len(suspeitos_vivos):
                alvo = suspeitos_vivos[escolha]
                objeto_alvo = jogo_contexto.dicionario_jogadores[alvo]
                
                if isinstance(objeto_alvo, Coringa):
                    print(f"\n🔍 [RESULTADO] Alvo Escolhido: {alvo} -> ⚠️ É O VILÃO! ⚠️")
                else:
                    print(f"\n🔍 [RESULTADO] Alvo Escolhido: {alvo} -> 👍 Ficha Limpa (Inocente) 👍")
            else:
                print("\nNenhuma pista coletada esta noite.")
        except ValueError:
            print("\nEntrada inválida. Turno de investigação perdido.")


class Coringa(Personagem):
    def __init__(self, nome: str):
        super().__init__(nome, papel="🤡 VILÃO (CORINGA)")

    # POLIMORFISMO: O Coringa elimina um tripulante
    def realizar_acao_noturna(self, jogo_contexto):
        print(f"\n🃏 [GÁS DO RISO] Vez do Vilão Secreto agir...")
        
        vitimas = [p for p in jogo_contexto.jogadores_ativos]
        
        for idx, nome in enumerate(vitimas, 1):
            print(f"  [{idx}] {nome}")
            
        try:
            escolha = int(input("\n(Vilão, digite o número da sua vítima em segredo): ")) - 1
            if 0 <= escolha < len(vitimas):
                alvo = vitimas[escolha]
                jogo_contexto.vitima_da_noite = alvo
                print(f"\n🎯 [Alvo Registado com Sucesso!]")
            else:
                print("\nO ataque falhou esta noite.")
        except ValueError:
            print("\nEntrada inválida. Ataque falhado.")


class Tripulante(Personagem):
    def __init__(self, nome: str):
        super().__init__(nome, papel="👥 TRIPULANTE INOCENTE")

    def realizar_acao_noturna(self, jogo_contexto):
        pass

# ==========================================
# 3. GERENCIADOR DO JOGO (INTERATIVO)
# ==========================================
class JogoCidadeDorme:
    def __init__(self):
        self.dicionario_jogadores = {} # Coleção OBRIGATÓRIA 1: DICIONÁRIO
        self.jogadores_actifs = set()   # Coleção OBRIGATÓRIA 2: CONJUNTO
        self.lista_nomes = []           # Coleção OBRIGATÓRIA 3: LISTA
        self.nome_batman_real = ""
        self.nome_coringa_real = ""
        self.vitima_da_noite = None

    @property
    def jogadores_ativos(self):
        return self.jogadores_actifs

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def cadastrar_participantes(self):
        self.limpar_tela()
        print("="*50)
        print(" 🦇 CADASTRO DE PARTICIPANTES - GOTHAM CITY 🦇 ")
        print("="*50)
        print("Digite o nome dos participantes que estão na mesa.")
        print("Quando terminar de adicionar todos, digite 'FIM'.\n")

        while True:
            nome = input(f"Nome do Participante #{len(self.lista_nomes) + 1}: ").strip()
            if nome.upper() == 'FIM':
                if len(self.lista_nomes) < 3:
                    print("❌ Adicione pelo menos 3 participantes para começar!")
                    continue
                break
            if nome == "":
                print("❌ O nome não pode ser vazio.")
                continue
            if nome in self.lista_nomes:
                print("❌ Esse nome já foi adicionado!")
                continue
            self.lista_nomes.append(nome)

        # Sorteio interno dos papéis em POO
        participantes_disponiveis = self.lista_nomes.copy()
        
        self.nome_batman_real = random.choice(participantes_disponiveis)
        participantes_disponiveis.remove(self.nome_batman_real)
        
        self.nome_coringa_real = random.choice(participantes_disponiveis)
        participantes_disponiveis.remove(self.nome_coringa_real)

        # Criação dos objetos das classes filhas
        for nome in self.lista_nomes:
            if nome == self.nome_batman_real:
                self.dicionario_jogadores[nome] = Batman(nome)
            elif nome == self.nome_coringa_real:
                self.dicionario_jogadores[nome] = Coringa(nome)
            else:
                self.dicionario_jogadores[nome] = Tripulante(nome)
            
            self.jogadores_ativos.add(nome)

        print(f"\n✅ {len(self.lista_nomes)} participantes registados!")
        input("Pressione ENTER para ir para a revelação secreta de papéis...")

    def fase_revelacao_papeis(self):
        """Nova função ajustada: Permite ver a função secreta de cada um igual no Werewolf de telemóvel"""
        self.limpar_tela()
        print("="*50)
        print(" 🐺 REVELAÇÃO DE PAPÉIS (ESTILO WEREWOLF) 🐺 ")
        print("="*50)
        opcao = input("Desejam descobrir as vossas funções secretas no ecrã agora? (s/n): ").strip().lower()
        
        if opcao == 's':
            for nome in self.lista_nomes:
                self.limpar_tela()
                print(f"📢 Vez de [{nome}] aproximar-se do ecrã!")
                input("Os outros desviam o olhar. Pressione [ENTER] quando estiver SOZINHO para ver o seu papel...")
                
                # Acessa o objeto em POO para extrair o papel sorteado pelo sistema
                personagem = self.dicionario_jogadores[nome]
                print(f"\n▶️ O teu papel secreto é: {personagem.papel} ◀️")
                
                input("\nPressione [ENTER] para APAGAR o ecrã antes que os outros vejam...")
            self.limpar_tela()
            print("✅ Todos os participantes já sabem as suas funções secretas! O jogo vai começar...")
        else:
            print("\n⏩ Pulando revelação. Certifiquem-se de que distribuíram os papéis por fora.")
        
        input("\nPressione ENTER para iniciar a primeira noite...")

    def fase_da_noite(self):
        self.limpar_tela()
        print("\n🌙 A CIDADE DORME... Todos na mesa fecham os olhos.")
        print("-" * 50)
        
        self.vitima_da_noite = None

        # 1. Turno do Coringa
        if self.nome_coringa_real in self.jogadores_ativos:
            input("\n[VILÃO] Quem for o VILÃO, abra os olhos e pressione [ENTER] (Os outros fecham os olhos)...")
            self.limpar_tela()
            self.dicionario_jogadores[self.nome_coringa_real].realizar_acao_noturna(self)
            input("\nPressione [ENTER] e feche os olhos novamente...")
            self.limpar_tela()
        
        # 2. Turno do Batman
        if self.nome_batman_real in self.jogadores_ativos:
            input("\n[INVESTIGADOR] Quem for o BATMAN, abra os olhos e pressione [ENTER] (Os outros fecham os olhos)...")
            self.limpar_tela()
            self.dicionario_jogadores[self.nome_batman_real].realizar_acao_noturna(self)
            input("\nPressione [ENTER] e feche os olhos novamente...")
            self.limpar_tela()

        if self.vitima_da_noite and self.vitima_da_noite in self.jogadores_ativos:
            self.jogadores_ativos.remove(self.vitima_da_noite)
            self.dicionario_jogadores[self.vitima_da_noite].status = "Eliminado"

    def fase_da_discussao_e_votacao(self):
        self.limpar_tela()
        print("\n☀️ A CIDADE ACORDA! Todos podem olhar para o ecrã!")
        print("="*50)
        
        if self.vitima_da_noite:
            print(f"💀 NOTÍCIA DE ÚLTIMA HORA: {self.vitima_da_noite} foi eliminado esta noite!")
        else:
            print("🕊️ Milagre em Gotham! Ninguém foi eliminado esta noite.")
            
        print("="*50)
        print(f"👥 Sobreviventes na mesa: {', '.join(self.jogadores_ativos)}")
        print("="*50)
        
        print("\nDebatam em conjunto quem vocês suspeitam que seja o Coringa infiltrado na mesa!")
        ativos_lista = list(self.jogadores_ativos)
        for idx, nome in enumerate(ativos_lista, 1):
            print(f"[{idx}] {nome}")
            
        try:
            voto = int(input("\nDigite o número de quem a mesa decidiu MANDAR para o Arkham: ")) - 1
            if 0 <= voto < len(ativos_lista):
                suspeito = ativos_lista[voto]
                
                self.dicionario_jogadores[suspeito].status = "Preso no Arkham"
                self.jogadores_ativos.remove(suspeito)
                
                print(f"\n🔒 {suspeito} foi enviado para o Asilo Arkham!")
                
                if suspeito == self.nome_coringa_real:
                    print("🎉 Parabéns! Vocês prenderam o verdadeiro Coringa!")
                else:
                    print(f"🤦‍♂️ Que erro! {suspeito} era apenas um Tripulante inocente!")
            else:
                print("Votação inconclusiva! Ninguém foi preso.")
        except ValueError:
            print("Voto inválido. Ninguém foi preso.")
            
        input("\nPressione ENTER para continuar para a próxima noite...")

    def verificar_vencedor(self):
        if self.nome_coringa_real not in self.jogadores_ativos:
            print("\n🏆 VITÓRIA DOS INOCENTES! O Coringa foi desmascarado e preso!")
            return True
        
        if len(self.jogadores_ativos) <= 2:
            print(f"\n🤡 VITÓRIA DO VILÃO! O Coringa ({self.nome_coringa_real}) conseguiu enganar toda a gente!")
            return True
            
        return False

    def jogar(self):
        self.cadastrar_participantes()
        self.fase_revelacao_papeis() # Ativação da fase de ver funções
        
        while True:
            self.fase_da_noite()
            if self.verificar_vencedor():
                break
                
            self.fase_da_discussao_e_votacao()
            if self.verificar_vencedor():
                break


if __name__ == "__main__":
    jogo = JogoCidadeDorme()
    jogo.jogar()