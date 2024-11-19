nome= input ('Qual é seu nome aluno?')
print ('Olá aluno {}, seja bem vindo ao programa de media final!'.format(nome))
n1 = float(input ('Qual foi sua nota do primeiro bimestre?'))
n2 = float(input ('Qual foi sua nota do segundo bimestre?'))
s = (n1 + n2) / 2
print('A media final é {:.1f}'.format(s))
print('Obrigado pelo desafio!')


