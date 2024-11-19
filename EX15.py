nome = input('Olá, qual é seu nome?')
print ('Seja bem vindo {}, este programa será sobre aluguel de carro.'.format(nome))
n0 = int(input ('Quantos dias o carro ficou alugado?'))
n1 = float(input ('Quantos Km rodados?'))
n2 = (n0 * 60) + (n1 * 0.15)
print ('O valor aluguel do carro ficou R${:.2f}.'.format(n2))
print ('Obrigado pelo deasafio!')

