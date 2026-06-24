import os
import random
from modelos.batman import Batman
from modelos.coringa import Coringa
from modelos.pinguim import Pinguim
from modelos.policial import Policial
from interfaces.inputs import ler_escolha_valida

def executar_cadastro(jogo):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*50)
    print(" 🦇 CADASTRO DE PARTICIPANTES - GOTHAM CITY 🦇 ")
    print("="*50)
    print("Digite o nome dos participantes. Digite 'FIM' para terminar.\n")

    while True:
        nome = input(f"Nome do Participante {len(jogo.lista_nomes) + 1}: ").strip()
        if nome.upper() == 'FIM':
            if len(jogo.lista_nomes) <= 3:
                print("❌ Adicione pelo menos 4 participantes para começar!")
                continue
            break
        if nome == "" or nome in jogo.lista_nomes:
            print("❌ Nome inválido ou já adicionado.")
            continue
        jogo.lista_nomes.append(nome)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*50)
    print(" 🎭 CONFIGURAÇÃO DE VILÕES 🎭 ")
    print("="*50)
    print(f"Total de participantes cadastrados: {len(jogo.lista_nomes)}")
    
    while True:
        qtd = ler_escolha_valida("Quantos vilões deseja ter nesta partida? (1 ou 2): ", 2)
        if qtd == 2 and len(jogo.lista_nomes) < 4:
            print("❌ Participantes insuficientes para 2 vilões! Selecione 1 vilão.")
            continue
        if qtd == 0:
            print("❌ O jogo precisa de pelo menos 1 vilão.")
            continue
        jogo.qtd_viloes_configurada = qtd
        break

    participantes_disponiveis = jogo.lista_nomes.copy()
    
    jogo.nome_batman_real = random.choice(participantes_disponiveis)
    participantes_disponiveis.remove(jogo.nome_batman_real)
    
    jogo.nome_coringa_real = random.choice(participantes_disponiveis)
    participantes_disponiveis.remove(jogo.nome_coringa_real)

    if jogo.qtd_viloes_configurada == 2:
        jogo.nome_pinguim_real = random.choice(participantes_disponiveis)
        participantes_disponiveis.remove(jogo.nome_pinguim_real)
    else:
        jogo.nome_pinguim_real = ""

    for nome in jogo.lista_nomes:
        if nome == jogo.nome_batman_real:
            jogo.dicionario_jogadores[nome] = Batman(nome)
        elif nome == jogo.nome_coringa_real:
            jogo.dicionario_jogadores[nome] = Coringa(nome)
        elif jogo.nome_pinguim_real and nome == jogo.nome_pinguim_real:
            jogo.dicionario_jogadores[nome] = Pinguim(nome)
        else:
            jogo.dicionario_jogadores[nome] = Policial(nome)
        
        jogo.jogadores_ativos.add(nome)

    print(f"\n✅ {len(jogo.lista_nomes)} participantes registados com sucesso!")
    print(f"🎮 Partida configurada com {jogo.qtd_viloes_configurada} vilão(ões).")
    input("\nPressione ENTER para ir para a revelação secreta...")