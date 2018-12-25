#CABEÇALHO
print('='*50)
print('{:^50}'.format('CAIXA ELETRÔNICO'))
print('='*50)

#Informa valor do saque
print('Notas disponíveis: R$50, R$20, R$10, R$1')
valor = int(input('Valor a ser sacado: R$'))

#Calculo de notas
qtd_notas = 0
nota = 50
total = valor
while valor > 0:
    if valor // nota > 0:
        qtd_notas = valor // nota
        print(f'{qtd_notas} notas de R${nota}')
        valor -= nota * qtd_notas
    elif nota == 50:
        nota = 20
    elif nota == 20:
        nota = 10
    elif nota == 10:
        nota = 1
    elif valor == 0:
        break

#DESPEDIDA
print('='*50)
print('OBRIGADO E VOLTE SEMPRE!!')
