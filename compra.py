print('COMPRA DO MÊS')
print('-='*30)
total = prod_caro = maior_preco = 0
while True:
    nome = str(input('nome: ')).strip().upper()
    preco = float(input('preço: '))

    total += preco

    if preco > 1000:
        prod_caro += 1

    if preco > maior_preco:
        maior_preco = preco
        mais_caro = nome

    print('-'*20)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
    if resp == 'N':
        print('-' * 20)
        break
    print('-'*20)
print(f'DADOS DA COMPRA:\n total: {total}\n {prod_caro} custam '
      f'mais que R$ 1000\n {mais_caro} é o produto mais caro, pois custa {maior_preco}.')

