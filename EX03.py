nome = input('Qual é seu nome?')
print ('Olá {},seja bem vindo(a) ao meu programa!'.format(nome))
print ('Neste programa irei executar um serie de calculos matematicos, com dois números que você me der.')
n1 = int(input('Digite um numero '))
n2 = int(input('Digite outro numero '))
soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
div = n1 / n2
divint = n1 // n2
e = n1 ** n2
print('A soma é {},a subtracão é {}, a multiplicacão é {},'.format(soma,sub,multi),end=' ')
print('a divisão é {:.3f}, a divisão inteira é {} e a potência {}.'.format(div,divint,e))
print('Obrigado pelo desafio!')






