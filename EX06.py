nome = input('Qual é seu nome?')
print ('Seja bem vindo {}, ao meu programa.'.format(nome))
print ('Eu vou criar um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.')
n1 = float(input('Qual é seu número?'))
dob = n1 * 2
tri = n1 * 3
raiz = n1 ** (1/2)
print('Seu número ao dobro é {}, seu número ao triplo é {} e seu número em raiz quadrada é {:.2f}.'.format(dob,tri,raiz))
print('Obrigado pelo desafio!')
