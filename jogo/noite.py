import os

def executar_fase_noite(jogo):
    jogo.limpar_tela()
    print("\n🌙 A CIDADE DORME... Todos na mesa fecham os olhos.")
    print("-" * 50)
    
    jogo.vitimas_da_noite.clear()
    jogo.jogador_silenciado = ""
    
    jogo.vitimas_da_noite.clear()

    if jogo.nome_coringa_real in jogo.jogadores_ativos:
        input("\n[VILÃO] Quem for o CORINGA, abra os olhos e pressione [ENTER]...")
        jogo.limpar_tela()
        jogo.dicionario_jogadores[jogo.nome_coringa_real].realizar_acao_noturna(jogo)
        input("\nPressione [ENTER] e feche os olhos...")
        jogo.limpar_tela()
    
    if jogo.nome_pinguim_real and jogo.nome_pinguim_real in jogo.jogadores_ativos:
        input("\n[VILÃO] Quem for o PINGUIM, abra os olhos e pressione [ENTER]...")
        jogo.limpar_tela()
        jogo.dicionario_jogadores[jogo.nome_pinguim_real].realizar_acao_noturna(jogo)
        input("\nPressione [ENTER] e feche os olhos...")
        jogo.limpar_tela()
    
    if jogo.nome_batman_real in jogo.jogadores_ativos:
        input("\n[INVESTIGADOR] Quem for o BATMAN, abra os olhos e pressione [ENTER]...")
        jogo.limpar_tela()
        jogo.dicionario_jogadores[jogo.nome_batman_real].realizar_acao_noturna(jogo)
        input("\nPressione [ENTER] e feche os olhos...")
        jogo.limpar_tela()

    for vitima in list(jogo.vitimas_da_noite):
        if vitima in jogo.jogadores_ativos:
            jogo.jogadores_ativos.remove(vitima)
            jogo.dicionario_jogadores[vitima].status = "Eliminado"