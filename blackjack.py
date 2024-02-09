import random

# Função para criar um baralho com 52 cartas
def criar_baralho():
    naipes = ['Copas', 'Espadas', 'Ouros', 'Paus']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    baralho = [(valor, naipe) for valor in valores for naipe in naipes]
    return baralho

# Função para calcular o valor de uma mão de cartas
def calcular_valor(mao):
    valor = 0
    ases = 0
    for carta in mao:
        if carta[0] in ['J', 'Q', 'K']:
            valor += 10
        elif carta[0] == 'A':
            ases += 1
            valor += 11
        else:
            valor += int(carta[0])
    
    # Ajuste para o valor dos Ases caso ultrapasse 21
    while valor > 21 and ases:
        valor -= 10
        ases -= 1
        
    return valor

# Função para exibir a mão de um jogador
def mostrar_mao(jogador, mao):
    print(f"{jogador} tem a mão:")
    for carta in mao:
        print(f" - {carta[0]} de {carta[1]}")

# Função para o jogo de Blackjack
def blackjack():
    baralho = criar_baralho()
    random.shuffle(baralho)
    
    mao_jogador = []
    mao_croupier = []
    
    # Distribuir cartas iniciais
    mao_jogador.append(baralho.pop())
    mao_croupier.append(baralho.pop())
    mao_jogador.append(baralho.pop())
    mao_croupier.append(baralho.pop())
    
    # Mostrar a mão inicial do jogador e uma carta do croupier
    mostrar_mao("Jogador", mao_jogador)
    print(f"Croupier tem a mão:")
    print(f" - {mao_croupier[0][0]} de {mao_croupier[0][1]}")
    
    # Verificar se o jogador já ganhou ou perdeu com as duas cartas iniciais
    if calcular_valor(mao_jogador) == 21:
        print("Blackjack! Você ganhou!")
        return
    elif calcular_valor(mao_croupier) == 21:
        print("Blackjack do Croupier! Você perdeu!")
        return
    
    # Loop para a vez do jogador
    while True:
        escolha = input("Deseja 'hit' ou 'stand'? ").lower()
        
        if escolha == 'hit':
            mao_jogador.append(baralho.pop())
            mostrar_mao("Jogador", mao_jogador)
            if calcular_valor(mao_jogador) > 21:
                print("Você estourou! Você perdeu!")
                return
        elif escolha == 'stand':
            break
    
    # Vez do croupier
    while calcular_valor(mao_croupier) < 17:
        mao_croupier.append(baralho.pop())
    
    # Mostrar a mão final do croupier
    print("Croupier tem a mão:")
    mostrar_mao("Croupier", mao_croupier)
    
    # Verificar resultado
    valor_jogador = calcular_valor(mao_jogador)
    valor_croupier = calcular_valor(mao_croupier)
    
    if valor_jogador > valor_croupier or valor_croupier > 21:
        print("Você ganhou!")
    elif valor_jogador < valor_croupier or valor_jogador > 21:
        print("Você perdeu!")
    else:
        print("Empate!")
    
# Executar o jogo
blackjack()
