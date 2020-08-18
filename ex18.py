from random import choice
a1 = str(input('Qual o nome do primeiro aluno?'))
a2 = str(input('Qual o nome do segundo?'))
a3 = str(input('Qual o nome do terceiro?'))
a4 = str(input('Qual o quarto?'))
lista = [a1, a2, a3, a4]
e = choice(lista)
print('O aluno sorteado foi {}'.format(e))
