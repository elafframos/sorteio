import random

print('\nSORTEIO DE NÚMEROS\n')

começo = int(input('Digite de onde vai começar o sorteio: '))
fim = int(input('Digite o último número do sorteio: '))
quantidade = int(input('Digite quantos números você deseja: '))

numeros = range(começo, fim)
sorteio = random.sample(numeros, quantidade)
print('\nO número sorteado é: {}\n'.format(sorteio))
