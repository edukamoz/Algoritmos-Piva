from os import system
from random import choice


def jogo():
    jogador = input('Digite sua escolha: ').lower()

    if jogador not in ['pedra', 'papel', 'tesoura']:
        print('\nEscolha inválida')
        quit()

    escolha = choice(['pedra', 'papel', 'tesoura'])

    print(f'''
    Jogador: {jogador.capitalize()}
    Máquina: {escolha.capitalize()}
    ''')
    if escolha == jogador:
        print('Empate!\n')
    elif ((escolha == 'pedra' and jogador == 'tesoura')
          or (escolha == 'tesoura' and jogador == 'papel')
          or (escolha == 'papel' and jogador == 'pedra')):
        print('Você perdeu!\n')
    else:
        print('Você ganhou!\n')


while True:
    system('cls')
    jogo()
    resposta = input('Deseja continuar? (s/n)')
    if resposta == 'n':
        print('\nObrigado por jogar!\n')
        quit()
