import math
nome = input("Olá, qual é seu nome?")
print  ("Seja bem vindo {},ao meu programa que calcúla a raiz quadrada de um número.".format(nome))
num = int(input('Digite um numero:'))
raiz = math.sqrt(num)
print ('A raiz de {} é igual a {}'.format(num,math.ceil(raiz)))

