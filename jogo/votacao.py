from interfaces.inputs import ler_escolha_valida

def executar_fase_votacao(jogo):
    jogo.limpar_tela()
    print("\n☀️ A CIDADE ACORDA!")
    print("="*50)
    
    if jogo.vitimas_da_noite:
        print(f"💀 NOTÍCIA DE ÚLTIMA HORA: {', '.join(jogo.vitimas_da_noite)} foram eliminados esta noite!")
    else:
        print("🕊️ Ninguém foi eliminado esta noite.")
        
    if jogo.jogador_silenciado in jogo.jogadores_ativos:
        print(f"🤫 EFEITO DO CORINGA: {jogo.jogador_silenciado} foi afetado pelo Gás do Riso e NÃO PODE falar nesta discussão!")
        
    print("="*50)
    print(f"👥 Sobreviventes na mesa: {', '.join(jogo.jogadores_ativos)}")
    print("="*50)
    
    ativos_lista = list(jogo.jogadores_ativos)
    print("  [0] Pular votação / Não prender ninguém no Arkham")
    for idx, nome in enumerate(ativos_lista, 1):
        print(f"  [{idx}] {nome}")
        
    voto = ler_escolha_valida("\nDigite o número de quem a mesa decidiu MANDAR para o Arkham: ", len(ativos_lista))
    
    if voto == 0:
        print("\nVotação inconclusiva! A cidade decidiu não prender ninguém hoje.")
    else:
        suspeito = ativos_lista[voto - 1]
        jogo.dicionario_jogadores[suspeito].status = "Preso no Arkham"
        jogo.jogadores_ativos.remove(suspeito)
        print(f"\n🔒 {suspeito} foi enviado para o Asilo Arkham!")
        
        if suspeito == jogo.nome_coringa_real and jogo.qtd_viloes_configurada == 2:
            jogo.coringa_ganhou_por_ejecao = True
            print(f"🃏 O Coringa ({jogo.nome_coringa_real}) começa a rir descontroladamente!")
            print("Ele queria ser pego para ativar o seu plano mestre!")
        elif suspeito in [jogo.nome_coringa_real, jogo.nome_pinguim_real]:
            print(f"🎉 Parabéns! Vocês prenderam um dos vilões infiltrados!")
        else:
            print(f"🤦‍♂️ Que erro! {suspeito} era apenas um Policial inocente!")
            
    input("\nPressione ENTER para continuar...")