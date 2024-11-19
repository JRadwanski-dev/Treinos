nome = input('Olá, qual é seu nome?')
print ('Seja bem vindo {}, ao programa de conversão de moedas!'.format(nome))
n0= float(input ('Coloque quanto de dinheiro você quer converter:'))
n1 = n0 / 3.27
print ('Caso coloque {} reais convertendo para dólar daria {:.2f} doláres.'.format(n0,n1))
print('Obrigado pelo desafio!')

