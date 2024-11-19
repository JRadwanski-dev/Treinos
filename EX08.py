nome = input('Olá, qual é seu nome?')
print ('Seja bem vindo {}, ao programa de conversão de medidas!'.format(nome))
n1 = float(input('Coloque em metros sua medida: '))
s = n1 * 100
p = n1 * 1000
print ('{} metros fica {} centímetros'.format(n1,s))
print ('{} metros fica {} milímitros' .format(n1,p))
print ('Obrigado pelo desafio!')