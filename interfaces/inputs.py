def ler_escolha_valida(mensagem: str, max_opcoes: int):
    while True:
        try:
            escolha = int(input(mensagem))
            if 0 <= escolha <= max_opcoes:
                return escolha
            print(f"❌ Opção inválida! Escolha um número entre 0 e {max_opcoes}.")
        except ValueError:
            print("❌ Entrada inválida! Por favor, digite apenas números.")