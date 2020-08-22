from random import shuffle
a1 = str(input('Qual o primeiro aluno?'))
a2 = str(input('Qual o segundo?'))
a3 = str(input("Qual o terceiro?"))
a4 = str(input('Qual o quarto?'))
l = [a1, a2, a3, a4]
shuffle(l)
print('A ordem da apresentação sera {}'.format(l))
