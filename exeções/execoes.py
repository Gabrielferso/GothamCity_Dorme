class PersonagemNoArkhamError(Exception):
    def __init__(self, nome):
        self.nome = nome
        super().__init__(f"🚨 {nome} está trancado no Asilo Arkham e não pode agir/ser alvo!")