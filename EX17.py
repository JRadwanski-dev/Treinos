import math
''''nome = input('OLá, qual é seu nome?')
print ('Seja bem vindo {}, este é um programa que calcula a hipotenusa.'.format(nome))
n1 = float (input ('Coloque o comprimento do cateto oposto:'))
n2 = float (input ('Coloque o comprimento do cateto adjacente:'))
n3 = (n1 ** 2 + n2 ** 2)**(1/2)
print ('O número da hipotenusa é {:.2f}.'.format(n3))'''
nome = input('OLá, qual é seu nome?')
print ('Seja bem vindo {}, este é um programa que calcula a hipotenusa.'.format(nome))
n1 = float (input ('Coloque o comprimento do cateto oposto:'))
n2 = float (input ('Coloque o comprimento do cateto adjacente:'))
hi = math.hypot(n1,n2)
print ('O número da hipotenusa é {:.2f}.'.format(hi))
