nome = input('Olá, qual é seu nome?')
print ('Seja bem vindo {}, este programa irá calcular o aumento do seu salário em 15%.'.format(nome))
n0 = float(input('Coloque seu salário atual:'))
n1 = (n0 * 15) / 100
n2 = n1 + n0
print ('Seu salário com reajuste de 15% ficará {:.2f}reais.'.format(n2))
print('Obrigado pelo desafio!')