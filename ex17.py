from math import tan, cos, sin, radians

a = float(input('digite um angulo'))
c = cos(radians(a))
t = tan(radians(a))
s = sin(radians(a))
print('Para o angulo {} a tangente é: {:.3f}, seno: {:.3f} e cosseno: {:.3f}'.format(a, t, s, c))
