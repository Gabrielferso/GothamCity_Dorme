class Local:
    def __init__(self, nome: str):
        self.nome = nome
        self.jogadores_no_local = set()  # CONJUNTO (Set) obrigatório do projeto

    def entrar_personagem(self, nome_personagem: str):
        self.jogadores_no_local.add(nome_personagem)

    def sair_personagem(self, nome_personagem: str):
        self.jogadores_no_local.discard(nome_personagem)