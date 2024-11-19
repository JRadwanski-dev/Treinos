nome = input ('Olá, qual é seu nome?')
print ('Seja bem vindo {}, ao meu programa de descontos.'.format(nome))
n0 = float(input('Coloque o preco do produto que desejar e o mesmo terá 5% de desconto:'))
n1 = (n0 * 5) /100
n2 = n0 - n1
print ('O valor do produto com desconto aplicado é {:.2f} reais.'.format(n2))
print('Obrigado pelo desafio!')
