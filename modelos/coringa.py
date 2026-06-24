from modelos.base import Personagem
from interfaces.inputs import ler_escolha_valida

class Coringa(Personagem):
    def __init__(self, nome: str):
        super().__init__(nome, papel="🤡 VILÃO (CORINGA)")

    def realizar_acao_noturna(self, jogo_contexto):
        print(f"\n🃏 [GÁS DO RISO] Vez do Coringa agir...")
        vitimas = [p for p in jogo_contexto.jogadores_ativos if p != self.nome]
        
        print("  [0] Pular turno / Não atacar ninguém")
        for idx, nome in enumerate(vitimas, 1):
            print(f"  [{idx}] {nome}")
            
        escolha = ler_escolha_valida("\n(Coringa, digite o número da sua escolha em segredo): ", len(vitimas))
        
        if escolha == 0:
            print("\nTurno pulado. Nenhum ataque realizado pelo Coringa.")
            return

        alvo = vitimas[escolha - 1]
        jogo_contexto.vitimas_da_noite.add(alvo)
        print(f"\n🎯 [Alvo Registado com Sucesso!]")