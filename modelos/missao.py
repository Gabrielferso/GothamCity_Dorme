class Missao:
    def __init__(self, descricao: str, localizacao: tuple):
        self.descricao = descricao
        self.localizacao = localizacao  
        self.concluida = False

    def finalizar(self):
        self.concluida = True