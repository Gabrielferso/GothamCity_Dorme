from abc import ABC, abstractmethod


class Personagem(ABC):
    def __init__(self, nome: str, papel: str):
        self.nome = nome
        self.papel = papel
        self.__status = "Ativo" 

    # Getter para acessar o status privado
    @property
    def status(self):
        return self.__status

    # Setter para alterar o status controladamente
    @status.setter
    def status(self, novo_status):
        if novo_status in ["Ativo", "Preso no Arkham", "Eliminado"]:
            self.__status = novo_status

    @abstractmethod
    def realizar_acao_principal(self):
        """Método abstrato que será polimórfico nas classes filhas."""
        pass


# HERANÇA: Criando a classe dos Aliados do Batman (Tripulação)
class Aliado(Personagem):
    def __init__(self, nome: str):
        super().__init__(nome, papel="Aliado")
        self.missoes_resolvidas = 0

    # POLIMORFISMO: Implementação específica do Aliado
    def realizar_acao_principal(self):
        return f"🔊 {self.nome} está patrulhando as ruas e resolvendo crimes!"


# HERANÇA: Criando a classe dos Vilões (Impostores)
class Vilao(Personagem):
    def __init__(self, nome: str):
        super().__init__(nome, papel="Vilão")
        self.sabotagens_realizadas = 0

    # POLIMORFISMO: Implementação específica do Vilão
    def realizar_acao_principal(self):
        return f"🤫 {self.nome} está agindo nas sombras para sabotar Gotham!"