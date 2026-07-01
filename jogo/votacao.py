import sys  # Importado para poder encerrar o jogo imediatamente com sys.exit()
from interfaces.inputs import ler_escolha_valida

def executar_fase_votacao(jogo):
    jogo.limpar_tela()
    print("\n☀️ A CIDADE ACORDA!")
    print("="*50)
    
    if jogo.vitimas_da_noite:
        print(f"💀 NOTÍCIA DE ÚLTIMA HORA: {', '.join(jogo.vitimas_da_noite)} foram eliminados esta noite!")
    else:
        print("🕊️ Ninguém foi eliminado esta noite.")
        
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
        
        # 1. Verifica se o suspeito era de fato um vilão
        if suspeito in [jogo.nome_coringa_real, jogo.nome_pinguim_real]:
            print(f"🎉 Parabéns! Vocês prenderam um dos vilões infiltrados!")
            
            # 2. CONTA QUANTOS VILÕES AINDA ESTÃO VIVOS NA MESA
            viloes_vivos = [v for v in [jogo.nome_coringa_real, jogo.nome_pinguim_real] if v in jogo.jogadores_ativos]
            
            # 3. SE NÃO RESTAR NENHUM VILÃO, O JOGO ACABA IMEDIATAMENTE
            if len(viloes_vivos) == 0:
                print("\n" + "="*50)
                print("🏆 FIM DE JOGO! TODOS OS VILÕES FORAM CAPTURADOS!")
                print("👮‍♂️ A polícia de Gotham venceu e a cidade está segura!")
                print("="*50)
                sys.exit() # Encerra a execução do script Python
                
        else:
            print(f"🤦‍♂️ Que erro! {suspeito} era apenas um Policial inocente!")
            
    input("\nPressione ENTER para continuar...")