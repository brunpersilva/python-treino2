from math import pow, sqrt
ca = float(input('Digite o valor de ca:'))
co = float(input('Digite valor de co'))
h = sqrt(pow(ca,2) + pow(co,2))
print('O valor da hipotenusa é {:.2f}'.format(h))