from math import sqrt, floor
nome = input("Olá, qual é seu nome?")
print  ("Seja bem vindo {},ao meu programa que calcúla a raiz quadrada de um número.".format(nome))
num = int(input('Digite um numero:'))
raiz = sqrt(num)
print ('A raiz de {} é igual a {}'.format(num,floor(raiz)))