from random import choice
lista = ['pedra', 'papel', 'tesoura']
escolha_pc = choice(lista)
escolha_user = str(input('JO-KEN-PÔ!: ')).lower()
if escolha_pc == escolha_user:
    print('EMPATE! o pc jogou: ', escolha_pc)
elif escolha_user == 'papel' and escolha_pc == 'pedra':
    print('VOCE GANHOU!! o pc jogou: ', escolha_pc)
elif escolha_user == 'tesoura' and escolha_pc == 'papel':
    print('VOCE GANHOU!! o pc jogou: ', escolha_pc)
elif escolha_user == 'pedra' and escolha_pc == 'tesoura':
    print('VOCE GANHOU!! o pc jogou: ', escolha_pc)
else:
    print('PERDEU! pc jogou: ', escolha_pc)
