nome = input('Olá, qual é seu nome?')
print ('Seja bem vindo {},ao meu programa que calcúla quantidade de tinta necessária para pintar uma parede!'.format(nome))
n0 = float(input('Coloque a largura em metros da parede que deseja pintar:'))
n1 = float(input('Coloque a altura em metros da parede que deseja pintar:'))
n2 = n0 * n1
print ('Sua parade tem uma área de {} metros quadrados, agora será feito o cálculo de quanta tinta será utilizada!'.format(n2))
n3 = n2 / 2
print ('Você terá que comprar {} litros de tinta'.format(n3))
print ('Obrigado pelo desafio!')