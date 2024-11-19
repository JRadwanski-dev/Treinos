import math
''''nome = input ('Olá, qual é seu nome?')
print ('Seja bem vindo {}, ao meu programa que irá lê um número real e transformar em inteiro'.format(nome))
n1 = float(input ('Coloque seu número real:'))
print ('O número {} tem a parte inteira {:.0f}.'.format(n1,n1))
print ('Obrigado pelo desafio {}.'.format(nome))'''

from math import trunc
num = float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua porcão inteira é {}'.format(num,trunc(num)))
