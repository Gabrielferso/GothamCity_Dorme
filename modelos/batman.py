from modelos.base import Personagem
from interfaces.inputs import ler_escolha_valida

class Batman(Personagem):
    def __init__(self, nome: str):
        super().__init__(nome, papel="🕵️‍♂️ DETETIVE (BATMAN)")

    def realizar_acao_noturna(self, jogo_contexto):
        print(f"\n🔬 [BAT-SINAL] Vez do Investigador Secreto agir...")
        suspeitos_vivos = [p for p in jogo_contexto.jogadores_ativos if p != self.nome]
        
        print("  [0] Pular turno / Não investigar ninguém")
        for idx, nome in enumerate(suspeitos_vivos, 1):
            print(f"  [{idx}] {nome}")
            
        escolha = ler_escolha_valida("\n(Investigador, digite o número da sua escolha em segredo): ", len(suspeitos_vivos))
        
        if escolha == 0:
            print("\nTurno pulado. Nenhuma pista coletada esta noite.")
            return

        alvo = suspeitos_vivos[escolha - 1]
        objeto_alvo = jogo_contexto.dicionario_jogadores[alvo]
        
        from modelos.coringa import Coringa
        from modelos.pinguim import Pinguim
        if isinstance(objeto_alvo, (Coringa, Pinguim)):
            print(f"\n🔍 [RESULTADO] Alvo Escolhido: {alvo} -> ⚠️ É UM VILÃO! ⚠️")
        else:
            print(f"\n🔍 [RESULTADO] Alvo Escolhido: {alvo} -> 👍 Ficha Limpa (Inocente) 👍")