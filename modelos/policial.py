from modelos.base import Personagem

class Policial(Personagem):
    def __init__(self, nome: str):
        super().__init__(nome, papel="👮 POLICIA DO DPGC")

    def realizar_acao_noturna(self, jogo_contexto):
        pass