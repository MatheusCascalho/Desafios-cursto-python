frase = input('Digite uma frase: ').lower().strip().split()
s = ''
frase = s.join(frase)
reversa = frase[::-1] #o operador [] fatia a string frase e o terceiro argumento (-1) indica o passo do fatiamento
palindromo = False
for c in range(0, len(frase)):
    if reversa[c] == frase[c]:
        palindromo = True
    else:
        palindromo = False
        break
print('É palindromo? {}\nfrase: {}\nreversa: {}'.format(palindromo,frase,reversa))
