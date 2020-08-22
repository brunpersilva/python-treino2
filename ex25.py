t = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes.'.format(t.count('A')))
print('O primeiro A aparece na posição: {} '.format(t.find('A')+1))
print('O ultimo A aparece na posição : {} '.format(t.rfind('A')+1))
