nome = input ('Olá, qual é seu nome?')
print ('Seja bem vindo {}, este é um programa que ira fazer a conversão de graus para fahrenheit. '.format(nome))
n0 = float(input('Informe a temperatura em ºC:'))
n1 = (n0 * 9/5) + 32
print ('A temperatura de {}ºC corresponde a {}ºF. '.format(n0,n1))
print ('Obrigado pelo desafio!')
