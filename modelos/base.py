from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome: str, papel: str):
        self.nome = nome
        self.papel = papel
        self.__status = "Ativo"  # Encapsulamento

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, novo_status):
        if novo_status in ["Ativo", "Preso no Arkham", "Eliminado"]:
            self.__status = novo_status

    @abstractmethod
    def realizar_acao_noturna(self, jogo_contexto):
        pass